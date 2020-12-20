#!/usr/bin/env python3
import pandas as pd
import os

df_census = pd.read_csv("data/output_Files/census/census.csv")
df_children = pd.read_csv("data/output_Files/crime/children.csv")
df_sc = pd.read_csv("data/output_Files/crime/sc.csv")
df_st = pd.read_csv("data/output_Files/crime/st.csv")
df_women = pd.read_csv("data/output_Files/crime/women.csv")

census_dist_list = list(df_census['STATE_DISTRICT'])

children = df_children.loc[df_children['STATE_DISTRICT'].isin(census_dist_list)].copy()
sc = df_sc.loc[df_sc['STATE_DISTRICT'].isin(census_dist_list)].copy()
st = df_st.loc[df_st['STATE_DISTRICT'].isin(census_dist_list)].copy()
women = df_women.loc[df_women['STATE_DISTRICT'].isin(census_dist_list)].copy()


for col in children.columns:
    if col == 'STATE_DISTRICT' or col == 'Year' :
        continue
    children.rename({col : 'children|'+col}, axis=1, inplace=True)
for col in sc.columns:
    if col == 'STATE_DISTRICT' or col == 'Year' :
        continue
    sc.rename({col : 'sc|'+col}, axis=1, inplace=True)
for col in st.columns:
    if col == 'STATE_DISTRICT' or col == 'Year' :
        continue
    st.rename({col : 'st|'+col}, axis=1, inplace=True)
for col in women.columns:
    if col == 'STATE_DISTRICT' or col == 'Year' :
        continue
    women.rename({col : 'women|'+col}, axis=1, inplace=True)

df_merged = pd.merge(children, sc, on=['STATE_DISTRICT', 'Year'])
df_merged = pd.merge(df_merged, st, on=['STATE_DISTRICT', 'Year'])
df_merged = pd.merge(df_merged, women, on=['STATE_DISTRICT', 'Year'])

# df_merged["STATE"] = df_merged.apply(lambda row: row.STATE_DISTRICT.split('_')[0], axis=1)
state = df_merged.apply(lambda row: row.STATE_DISTRICT.split('_')[0], axis=1)
df_merged.insert(loc=1, column='STATE', value=state)
df_merged.to_csv("merged_crime_dataset.csv", index=None)