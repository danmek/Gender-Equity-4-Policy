
# NOTE
# earnings-raw.csv is raw data downloaded from Bureau of Labor Statistics (BLS). 
# earnings-id.csv is a file I generated myself, where I looked up the SeriesID and added notes on relevant aspects of each Series ID.
# This script combines the two into a earnings.csv file that I will work with in other python scripts. 

import csv
from pprint import pprint


# 1. add descriptions of seriesid into the raw data to enable lookup

# read csv files
with open('earnings-raw.csv', 'r') as f:
    reader = csv.DictReader(f)
    labor_raw = list(reader)

with open('earnings-id.csv', 'r') as f:
    reader = csv.DictReader(f)
    labor_id = list(reader)

# confirming headers
# print(labor_id[0].keys()) #['seriesid', 'children', 'sex', 'maritalstatus']
# print(labor_raw[0].keys())  #['SeriesID', 'Year', 'Period', 'Label', 'Value', '12-Month Net Change', '12-Month % Change'])

# copy raw data into a new list, which will include the information from labor_id
labor_raw_id = labor_raw

# look up the id from labor_raw and add descriptions from labor_id. 
for row_data in labor_raw_id:
	for row_id in labor_id:
		if row_id['seriesid'] == row_data['SeriesID']:
			row_data['Children'] = row_id['children']
			row_data['Gender'] = row_id['sex']
			row_data['MaritalStatus'] = row_id['maritalstatus']


# create new csv file with the ids
with open('earnings.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(labor_raw_id[0].keys())
    for i in labor_raw_id:
        writer.writerow(i.values())