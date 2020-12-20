#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

file_name = "merged_crime_dataset.csv"
df = pd.read_csv(file_name)

dist_set = set(df["STATE_DISTRICT"])
crime_list = df.columns


for dist in dist_set :
    temp_df = df.loc[df['STATE_DISTRICT'] == dist]
    for crime in crime_list :
        if crime == "STATE_DISTRICT" or crime == "Year" or crime == "STATE" :
            continue
        Path("dataforregression_district_wise/" + dist).mkdir(parents=True, exist_ok=True)
        temp1_df = temp_df[['Year', crime]]
        temp1_df.to_csv("dataforregression_district_wise/" + dist + '/' + crime+'.csv', index=None)


df["STATE"] = df.apply(lambda row: row.STATE_DISTRICT.split('_')[0], axis=1)

df.drop('STATE_DISTRICT', axis=1, inplace=True)
df = df.groupby(["STATE", "Year"]).sum().reset_index()


state_set = set(df["STATE"])
crime_list = df.columns


for state in state_set :
    temp_df = df.loc[df['STATE'] == state]
    for crime in crime_list :
        if crime == "STATE_DISTRICT" or crime == "Year" or crime == "STATE" :
            continue
        Path("dataforregression_state_wise/" + state).mkdir(parents=True, exist_ok=True)
        temp1_df = temp_df[['Year', crime]]
        temp1_df.to_csv("dataforregression_state_wise/" + state + '/' + crime+'.csv', index=None)


df.drop('STATE', axis=1, inplace=True)
df = df.groupby(["Year"]).sum().reset_index()


year_set = set(df["Year"])
crime_list = df.columns


for year in year_set :
    temp_df = df.loc[df['Year'] == year]
    for crime in crime_list :
        if crime == "STATE_DISTRICT" or crime == "Year" or crime == "STATE" :
            continue
        Path("dataforregression_country_wise/" + str(year)).mkdir(parents=True, exist_ok=True)
        temp1_df = temp_df[['Year', crime]]
        temp1_df.to_csv("dataforregression_country_wise/" + str(year) + '/' + crime+'.csv', index=None)
