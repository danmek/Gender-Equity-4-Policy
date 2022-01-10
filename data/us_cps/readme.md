Current Population Survey (CPS) 

Source: US Census Bureau

Example of data included:
- employment rate by sex
- reasons for unemployment 

Key takeaways:
- Reasons for unemployment by gender --> Women are unemployed due to family and home responsibilities far more than men. However, this requires use of underlying raw data, which my Excel can't handle (but may be possible with python). Historical trends may also be interesting. 
- Unemployment rate by gender and occupation --> But no meaningful difference in women in professional occupations vs. men, so not very helpful. We may be able to find meaningful difference in the raw data, but same issue as above. 

Some analysis done by Brookings here from the same dataset, but from 2018. : https://www.brookings.edu/research/labor-force-nonparticipation-trends-causes-and-policy-solutions/#cancel

Raw survey data source: https://www.census.gov/data/datasets/2021/demo/cps/cps-asec-2021.html

Analyzed tables source: https://www.bls.gov/cps/tables.htm

Files guide:
- datadict_cpsmar21.pdf: Data dictionary
- us_cps_2020: full set of analyzed tables
- us_cps_selected_2020: selected subset of tables from above file
- us_cps_raw_...: raw survey data at the household, family, and persons level. BUT repwgt and persons too large for GitHub and is not included here. 


