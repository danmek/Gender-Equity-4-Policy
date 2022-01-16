----->Data Sources and Steps<------
Worldwide: Gender wage gap: Employees, Percentage, 2020 or latest available
https://www.oecd-ilibrary.org/employment/gender-wage-gap/indicator/english_7cee77aa-en?isPartOf=/content/indicatorgroup/4ead40c7-en 

Education: Median weekly earnings, 2020
https://www.bls.gov/opub/reports/womens-databook/2020/home.htm 

Occupation: Number of full-time workers and median annual earnings of full-time workers by occupation, US Census Bureau 2019 https://www.dol.gov/agencies/wb/data/occupations 

States/Political Party: 
State: Median usual weekly earnings of full-time wage and salary workers, by state, 2020 annual averages
https://www.bls.gov/opub/reports/womens-earnings/2020/ 

Political: leaning by presidential election 2020 - The American Presidency Project, UCSB
 https://www.presidency.ucsb.edu/statistics/elections/2020 



---->readme-wage-OECD<-----
#Go to: https://tinyurl.com/3pwk92bb to access the raw OECD data (original URL path shortened using TinyURL)

#Scroll down to the bar chart titled “Gender wage gap: Employees, Percentage, 2020 or latest available”

#Note that the webpage should default to showing data from 2017-2020 (or most recent year for which they have data), but you can adjust the sliding scale to 2017-2020, if not the case

#Click the “Download” button on the top right hand corner of the chart and click on “selected data only (.csv)” from the dropdown menu. 

#Open the downloaded csv file named DP_LIVE_15012022084229707.csv

#Delete columns C-E inclusive and column H (remaining should be the columns with headers “LOCATION”, “TIME” and “Value”)

#We will now remove duplicate values for each country, leaving only the most recent gender wage gap percentage available for each unique country
>>>Copy and paste entire column A into empty column D
>>>Select all the pasted values in column D and click “Data” and “Remove Duplicates”
>>>Choose “Continue with the current selection” when pop-up dialogue appears
>>>Click “Remove Duplicates” and select “Remove Duplicates” again when the pop-up dialogue confirms action with number of duplicates found
>>>Select the empty cell E2 and enter this formula: =MAX(IF($A$2:$A$104=D2,$B$2:$B$104))
>>>Select cell E2 and drag fill down to the cell you need by clicking on the bottom right hand corner of the cell and dragging the cursor down along the column 
>>>What you have now in columns D and E are deduped countries (column D) with the corresponding year for the most recent data point available (E)
>>>You may want to give columns D and E a new header name like “Unique Country” and “Recent Year” respectively, for example

#Next, we will want to V-lookup the values for each unique country, but this would require running v-lookup based on multiple criteria (both LOCATION and TIME values), so the following steps are a simple way to achieve this:
>>>Insert a new column between B and C (your current headers from A-F with corresponding data should read “LOCATION”, “TIME”, [empty], “Value”, “Unique Country” and “Recent Year)
>>>In cell C2, enter this formula: =CONCATENATE(A2, B2)
>>>You should see “AUS2017” in C2. Drag fill down column C from there to completed a  concatenated list of values from columns A and B
>>>We will do the same for our list of unique countries by entering the following formula in cell G2: =CONCATENATE(E2, F2)
>>>At this point, select all > copy > paste special > values. This will copy and paste the concatenated string as text and not a formula
>>>We are finally ready to V-lookup! In cell H2, enter the following formula: ​​=VLOOKUP(@G:G, C:D, 2, FALSE)
>>>Drag fill down from H2 down to H46
>>>(again) Select all > copy > paste special > value
>>>Give column H a new header like “Wage Gap”

#Delete columns A-D and F-G inclusive. You should now have “Unique Country” in column A and “Wage Gap” in column B

#To get the full name of the country, rather than just the country code, copy and paste the list on this website: https://tinyurl.com/3uec28cu into column C. We will need to extract the code and country name from the concatenated text. To do this, follow these steps:
>>>Paste =LEFT(C2, 3) in D2 and drag fill down for the code
>>>Paste =REPLACE(C2,1,4,"") in E2 and drag fill down for the country name
>>>Copy all and paste special for values, as in previous steps

#Delete column C containing the combined text

#Run a V-lookup to apply the extracted full country name next to the corresponding wage gap. Select all, copy, and paste special.

#Sort the data according to wage gap and delete columns that do not contain the full country name nor wage gap data

#Give remaining columns proper headers, as you’d like them to appear on your chart

#Select all data and go to Insert > Chart > Bar

#Adjust stylistic changes as preferred and voila!

---->readme-wage-education<-----
#Get the data from: https://www.bls.gov/opub/reports/womens-databook/2020/home.htm 

#In an Excel sheet, create three columns with headers: “Educational Attainment”, “Women”, and “Men”

#Extract data for the levels of education you’d like represented in your graph. My chart used the following: ​​Less than a high school diploma, High school graduate, no college, Some college, no degree, Associate's degree, Bachelor's degree, Master's degree, Professional degree, Doctoral degree

#Record the corresponding figures for men and women by educational attainment in the “Men” and “Women” column respectively.

#Select the data and click Insert > Chart > Stacked Bar

#Adjust labels and style as preferred

---->readme-wage-occupation<----
#Data can be found here: https://www.dol.gov/agencies/wb/data/occupations 

#In an Excel file, sort the data by “median earnings” to identify the top highest and lowest pay jobs

#Determine how many occupations you’d like represented on your graph and pick from the top and bottom values for the extremes. In my case, I picked top and bottom 5.

#Delete the other rows in between for your ease

#Delete all columns except “Occupation”, “Median earnings women” and “Median earnings Men”

#Select the data and go to Insert > Chart > Clustered Column

#Format numbers under Format > numbers > currency

#Adjust labels and style as preferred

