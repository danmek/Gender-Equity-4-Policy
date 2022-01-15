# This script is run after earnings.py, which creates the file I call in this python script

# Data for D3 visualzation - earnings by gender and age of children

import csv
from pprint import pprint

# 1. read csv file 

with open('earnings.csv', 'r') as f:
    reader = csv.DictReader(f)
    earnings = list(reader)

# confirming headers
# print(earnings[0].keys())
#['seriesid', 'Year', 'Period', 'Label', 'Value', '12-Month Net Change', '12-Month % Change', 'Children', 'Gender', 'MaritalStatus']

# 2. Initialize the list which will become the csv for D3

headers = ['ChildrenAge', 'Men', 'Women']
row_names = ['under 6', '6 to 17', 'under 18']

earnings_d3 = [] 

earnings_d3.append(headers)

for i in row_names:
	earnings_d3.append([i, 0, 0])

# 3. Choose relevant data series

# Men, under 18, "Married, spouse present"
# Men, under 18, "All other statuses"
# Women, under 18, "Married, spouse present"
# Women, under 18, "All other statuses"

count = 0 # double check for duplicates

for row_data in earnings:
	if row_data['MaritalStatus'] == 'N/A' and row_data['Label'] == '2020 Annual':
		if row_data['Children'] == "under 6" and row_data['Gender'] == 'Men':
			earnings_d3[1][1]= row_data['Value']
			count = count + 1
		elif row_data['Children'] == "under 6" and row_data['Gender'] == 'Women':
			earnings_d3[1][2]= row_data['Value']
			count = count + 1
		if row_data['Children'] == "6 to 17" and row_data['Gender'] == 'Men':
			earnings_d3[2][1]= row_data['Value']
			count = count + 1
		elif row_data['Children'] == "6 to 17" and row_data['Gender'] == 'Women':
			earnings_d3[2][2]= row_data['Value']
			count = count + 1		
		if row_data['Children'] == "under 18" and row_data['Gender'] == 'Men':
			earnings_d3[3][1]= row_data['Value']
			count = count + 1
		elif row_data['Children'] == "under 18" and row_data['Gender'] == 'Women':
			earnings_d3[3][2]= row_data['Value']
			count = count + 1

earnings_d3_dict = []

for i in earnings_d3[1:]:
	d = {k:v for k,v in zip(headers, i)}
	earnings_d3_dict.append(d)

# pprint(earnings_d3_dict)

# 5. create new csv file 
with open('earnings-children.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(earnings_d3_dict[0].keys())
    for i in earnings_d3_dict:
        writer.writerow(i.values())