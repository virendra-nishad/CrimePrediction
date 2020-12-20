#!/usr/bin/env python3
import pandas as pd
import os
import csv
import numpy as np
from sklearn.linear_model import LinearRegression


temp_df = pd.read_csv("merged_crime_dataset.csv")
cols = list(temp_df.columns)
# print(cols)
cols.remove("Year")
cols.remove("STATE")
path = os.getcwd()
path = os.path.join(path, "dataforregression_district_wise")
districts = os.listdir(path)

predicted_crime = []

for dist in districts :
    temp_dict = {}
    temp_dict['STATE_DISTRICT'] = dist
    inner_path = os.path.join(path, dist)
    crime_csvfiles = os.listdir(inner_path)
    for files in crime_csvfiles :
        fname = os.path.join("dataforregression_district_wise", dist, files)
        if os.path.isfile(fname) :
            df_crime = pd.read_csv(fname)
            x = df_crime.iloc[:, 0].values
            y = df_crime.iloc[:, 1].values
            regressor = LinearRegression()
            regressor.fit(x.reshape(-1, 1), y)
            test = np.array([2011])
            prediction = regressor.predict(test.reshape(-1, 1))
            if int(prediction) <= 0 :
                ans = 0
            else :
                ans = int(prediction)

            temp1 = files.split('.')
            crime_name = temp1[0]
            # print(crime_name, ans)
            temp_dict[crime_name] = ans
    predicted_crime.append(temp_dict)
    
with open("2011_crime_prediction_district.csv", 'w') as csvfile :
    writer = csv.DictWriter(csvfile, fieldnames=cols)
    writer.writeheader()
    writer.writerows(predicted_crime)

df = pd.read_csv("2011_crime_prediction_district.csv")
df.sort_values('STATE_DISTRICT', inplace=True)
df.to_csv("2011_crime_prediction_district.csv", index=None)

############################################################################################


cols = list(temp_df.columns)
cols.remove("Year")
cols.remove("STATE_DISTRICT")

path = os.getcwd()
path = os.path.join(path, "dataforregression_state_wise")
states = os.listdir(path)

predicted_crime = []

for state in states :
    temp_dict = {}
    temp_dict['STATE'] = state
    inner_path = os.path.join(path, state)
    crime_csvfiles = os.listdir(inner_path)
    for files in crime_csvfiles :
        fname = os.path.join("dataforregression_state_wise", state, files)
        if os.path.isfile(fname) :
            df_crime = pd.read_csv(fname)
            x = df_crime.iloc[:, 0].values
            y = df_crime.iloc[:, 1].values
            regressor = LinearRegression()
            regressor.fit(x.reshape(-1, 1), y)
            test = np.array([2011])
            prediction = regressor.predict(test.reshape(-1, 1))
            if int(prediction) <= 0 :
                ans = 0
            else :
                ans = int(prediction)

            temp1 = files.split('.')
            crime_name = temp1[0]
            # print(crime_name, ans)
            temp_dict[crime_name] = ans
    predicted_crime.append(temp_dict)
    
with open("2011_crime_prediction_state.csv", 'w') as csvfile :
    writer = csv.DictWriter(csvfile, fieldnames=cols)
    writer.writeheader()
    writer.writerows(predicted_crime)

df = pd.read_csv("2011_crime_prediction_state.csv")
df.sort_values('STATE', inplace=True)
df.to_csv("2011_crime_prediction_state.csv", index=None)

############################################################################################



cols = list(temp_df.columns)
cols.remove("STATE")
cols.remove("STATE_DISTRICT")

path = os.getcwd()
path = os.path.join(path, "dataforregression_country_wise")
years = os.listdir(path)

predicted_crime = []

for year in years :
    temp_dict = {}
    temp_dict['Year'] = year
    inner_path = os.path.join(path, year)
    crime_csvfiles = os.listdir(inner_path)
    for files in crime_csvfiles :
        fname = os.path.join("dataforregression_country_wise", year, files)
        if os.path.isfile(fname) :
            df_crime = pd.read_csv(fname)
            x = df_crime.iloc[:, 0].values
            y = df_crime.iloc[:, 1].values
            regressor = LinearRegression()
            regressor.fit(x.reshape(-1, 1), y)
            test = np.array([2011])
            prediction = regressor.predict(test.reshape(-1, 1))
            if int(prediction) <= 0 :
                ans = 0
            else :
                ans = int(prediction)

            temp1 = files.split('.')
            crime_name = temp1[0]
            # print(crime_name, ans)
            temp_dict[crime_name] = ans
    predicted_crime.append(temp_dict)
    
with open("2011_crime_prediction_year.csv", 'w') as csvfile :
    writer = csv.DictWriter(csvfile, fieldnames=cols)
    writer.writeheader()
    writer.writerows(predicted_crime)
df = pd.read_csv("2011_crime_prediction_year.csv")
df.sort_values('Year', inplace=True)
df.to_csv("2011_crime_prediction_year.csv", index=None)
#############################################################################################
