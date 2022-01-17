# This script is run after labor.py, which creates the file I call in this python script

# Data for D3 visualzation - labor force participation by gender and age of children
# Note: the script is the same across labor-children.py, labor-married.py, and earnings-children.py, but with different arguments.

import csv
from pprint import pprint
import pandas as pd

# 1. read csv file 

with open('earnings.csv', 'r') as f:
    reader = csv.DictReader(f)
    earnings = list(reader)

# confirming headers
# print(labor[0].keys())
#['seriesid', 'Year', 'Period', 'Label', 'Value', '12-Month Net Change', '12-Month % Change', 
# 'Children', 'Gender', 'MaritalStatus']

df_raw = pd.DataFrame(earnings)

# 2. initialize headers & rows - the csv file that is required for the D3 visualization

headers = ['Children', 'Men', 'Women']
row_names = ['under 6', '6 to 17', 'under 18']
category = 'Gender'

# 3. create a dataframe that will become csv for d3

data_d3 = []

row = []
for r in row_names:
	row = [r]
	for h in headers[1:]:
		row.append(0)
	data_d3.append(row)

df_d3 = pd.DataFrame(data_d3, columns=headers)

# pprint(df_d3)
# pprint(list(df_d3.columns))

# 3. filter for the rows I need

whitelist_label = ['2020 Annual'] # year, period, label all refer to same things in this dataset
whitelist_children = ['under 6', '6 to 17', 'under 18']
whitelist_gender = ['Men', 'Women']
whitelist_status = 'N/A'

df_raw = df_raw.query('Label in @whitelist_label')
df_raw = df_raw.query('Children in @whitelist_children')
df_raw = df_raw.query('Gender in @whitelist_gender')
df_raw = df_raw.query('MaritalStatus in @whitelist_status')

# pprint(df_raw.head())

# 4. add values of the filtered rows into the corresponding dataframe

# looping through raw data
# if the raw data matches the row_names and category, add 
for index in df_raw.index:
	for r in row_names:
		if df_raw.loc[index, headers[0]]==r:
			for h in headers[1:]:
				if df_raw.loc[index, category] == h:
					df_d3.loc[row_names.index(r), h] = df_raw.loc[index, 'Value']

# print(df_d3)

# 5. write out csv 

df_d3.to_csv('earnings-children.csv', index=False)
