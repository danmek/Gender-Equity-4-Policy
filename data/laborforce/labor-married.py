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

# 2. Initialize the list which will become the csv for D3

headers = ['Gender', 'Married, spouse present', 'All other statuses']
row_names = ['Men', 'Women']

labor_d3 = [] 

labor_d3.append(headers)

for i in row_names:
	labor_d3.append([i, 0, 0])

# 3. Choose relevant data series

# Men, under 18, "Married, spouse present"
# Men, under 18, "All other statuses"
# Women, under 18, "Married, spouse present"
# Women, under 18, "All other statuses"

count = 0 # double check for duplicates

for row_data in labor:
	if row_data['Children'] == 'under 18' and row_data['Label'] == '2020 Annual':

		if row_data['Gender'] == "Men" and row_data['MaritalStatus'] == "Married, spouse present":
			labor_d3[1][1] = row_data['Value']
			count = count + 1

		elif row_data['Gender'] == "Women" and row_data['MaritalStatus'] == "Married, spouse present":
			labor_d3[2][1] = row_data['Value']
			count = count + 1
		
		elif row_data['Gender'] == "Men" and row_data['MaritalStatus'] == "All other statuses":
			labor_d3[1][2] = row_data['Value']
			count = count + 1

		elif row_data['Gender'] == "Women" and row_data['MaritalStatus'] == "All other statuses":
			labor_d3[2][2] = row_data['Value']
			count = count + 1

# pprint(labor_d3)
# pprint(count)


# 4. convert into dictionary

 # blank dictionary with only keys 

# rows = []
# row = []

# for r in row_names:
# 	for h in headers:
# 		if h == headers[0]:
# 			row.append(r)
# 		else:
# 			row.append(None)
# 	rows.append(row)
# 	row = []

labor_d3_dict = []

for i in labor_d3[1:]:
	d = {k:v for k,v in zip(headers, i)}
	labor_d3_dict.append(d)

# pprint(labor_d3_dict)

# 5. create new csv file 
with open('labor-married.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(labor_d3_dict[0].keys())
    for i in labor_d3_dict:
        writer.writerow(i.values())