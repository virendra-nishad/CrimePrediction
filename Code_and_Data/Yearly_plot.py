#!/usr/bin/env python3

import json
import csv
import pandas
import matplotlib.pyplot as plt
import os


file_name = "2011_crime_prediction_year.csv"
crime_df = pandas.read_csv(file_name)
crimes = list(crime_df.columns)
crimes.remove("Year")


for crime in crimes:
    fig = plt.bar(crime_df["Year"], crime_df[crime])
    plt.ylabel("Crime count")
    plt.xlabel(crime)

    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, "yearly-crime-plot")
    if not os.path.exists(path):
        os.mkdir(path)
    fig_name = crime + ".png"
    plt.savefig(os.path.join(path, fig_name))
    plt.clf()