# This script is run after labor.py, which creates the file I call in this python script

# Data for D3 visualzation - labor force participation by gender and marital status 

import csv
from pprint import pprint

# 1. read csv file 

with open('labor.csv', 'r') as f:
    reader = csv.DictReader(f)
    labor = list(reader)

# confirming headers
headers = list(labor[0].keys())
# print(headers)
# ['seriesid', 'Year', 'Period', 'Label', 'Value', '12-Month Net Change', '12-Month % Change', 'Children', 'Gender', 'MaritalStatus']

# 2. Filter for rows of the data I need

# Men, under 18, "Married, spouse present", 2020 Annual
# Men, under 18, "All other statuses", 2020 Annual
# Women, under 18, "Married, spouse present", 2020 Annual
# Women, under 18, "All other statuses", 2020 Annual

whitelist_gender = ['Men', 'Women']
whitelist_label = ['2020 Annual']
whitelist_status = ['Married, spouse present', 'All other statuses']
whitelist_children = ['under 18']

labor_d3_filtered = []

for i in labor:
	if i['Gender'] in whitelist_gender and i['Label'] in whitelist_label and i['MaritalStatus'] in whitelist_status and i['Children'] in whitelist_children:
		labor_d3_filtered.append(i)

#pprint(labor_d3_filtered)

# 3. Filter for the columns of data I need

whitelist_headers = ['Value', 'Gender', 'MaritalStatus']
blacklist_headers = []

for i in headers:
	if i not in whitelist_headers:
		blacklist_headers.append(i)

for i in labor_d3_filtered:
	for j in blacklist_headers:
		i.pop(j, None)

pprint(labor_d3_filtered)

# 4. Format into different dictionary

labor_d3_headers  = ['Marital Status', 'Men', 'Women']
labor_d3_rows = ['Married, spouse present', 'All other statuses']

labor

### WIP