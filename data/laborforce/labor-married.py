# This script is run after labor.py, which creates the file I call in this python script

# Data for D3 visualzation - labor force participation by gender and marital status 

import csv
from pprint import pprint

# 1. read csv file 

with open('labor.csv', 'r') as f:
    reader = csv.DictReader(f)
    labor = list(reader)

# confirming headers
# print(labor[0].keys())
#['seriesid', 'Year', 'Period', 'Label', 'Value', '12-Month Net Change', '12-Month % Change', 'Children', 'Gender', 'MaritalStatus']


# 2. Headers for the csv that is needed for D3

headers = ['Marital Status', 'Men', 'Women']

# 3. Create list for the csv that is needed for D3
labor_married = {}

for h in headers:
	labor_married[h] = None

pprint(labor_married)

# 3. Choose relevant data series

# Men, under 18, "Married, spouse present"
# Men, under 18, "All other statuses"
# Women, under 18, "Married, spouse present"
# Women, under 18, "All other statuses"

checkcount = 0

for row_data in labor:
	if row_data['Gender'] == "Men" and row_data['Children'] == "under 18" and row_data['MaritalStatus'] == "Married, spouse present" and row_data['Label'] == "2020 Annual":
		labor_married['Marital Status'] = row_data['MaritalStatus']
		labor_married['Men'] = row_data['Value']
		checkcount = checkcount+1
	if row_data['Gender'] == "Men" and row_data['Children'] == "under 18" and row_data['MaritalStatus'] == "All other statuses" and row_data['Label'] == "2020 Annual":
		labor_married['Marital Status'] = row_data['MaritalStatus']
		labor_married['Men'] = row_data['Value']
		checkcount = checkcount+1
	if row_data['Gender'] == "Women" and row_data['Children'] == "under 18" and row_data['MaritalStatus'] == "Married, spouse present" and row_data['Label'] == "2020 Annual":
		labor_married['Marital Status'] = row_data['MaritalStatus']
		labor_married['Women'] = row_data['Value']
		checkcount = checkcount+1
	if row_data['Gender'] == "Women" and row_data['Children'] == "under 18" and row_data['MaritalStatus'] == "All other statuses" and row_data['Label'] == "2020 Annual":
		labor_married['Marital Status'] = row_data['MaritalStatus']
		labor_married['Women'] = row_data['Value']
		checkcount = checkcount+1

pprint(labor_married)
pprint(checkcount)


# # 1. add descriptions of seriesid into the raw data to enable lookup

# # read csv files
# with open('labor-raw.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     labor_raw = list(reader)

# with open('labor-id.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     labor_id = list(reader)



# # copy raw data into a new list, which will include the information from labor_id
# labor_raw_id = labor_raw

# # look up the id from labor_raw and add descriptions from labor_id. 
# for row_data in labor_raw_id:
# 	for row_id in labor_id:
# 		if row_id['seriesid'] == row_data['seriesid']:
# 			row_data['Children'] = row_id['children']
# 			row_data['Gender'] = row_id['sex']
# 			row_data['MaritalStatus'] = row_id['maritalstatus']


# # create new csv file with the ids
# with open('labor.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(labor_raw_id[0].keys())
#     for i in labor_raw_id:
#         writer.writerow(i.values())