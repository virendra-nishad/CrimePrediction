#!/bin/sh

echo "started ..."

cd Code_and_Data

python3 merging_crime_dataset.py
python3 generating_regression_data.py
python3 predicting_crimes.py
python3 Yearly_plot.py

echo "Generating RESULTS ..."

cp 2011_crime_prediction_district.csv ../
cp 2011_crime_prediction_state.csv ../
cp 2011_crime_prediction_year.csv ../
cp -r yearly-crime-plot ../
echo "Finished ..."
