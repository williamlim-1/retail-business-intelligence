# Data Generation Folder

## What This Folder Is:
This folder contains the Python script I used to generate the mock retail datasets for the Business Intelligence project.

The goal was to simulate a realistic point-of-sale (POS) data export from a multi-store retail company. Instead of using a public dataset, I built one from scratch to better control structure, scale, and data quality issues.

## Script Included:
`generate-retail-data.py`

## What the Script Does
The script generates:
- 250,000+ transactions
- 60 stores across 4 regions (West, Midwest, South, Northeast)
- 1,200 products across 10+ categories
- 25,000 customers
- 2 years of historical transaction data (2023–2024)

The data was designed to support analysis of revenue, profit margins, promotions, regional trends, and seasonality.

## Why I Injected Data Issues
To make the project more realistic, I intentionally added some common data quality problems you would see in real exports:
- Mixed timestamp formats
- Inconsistent category casing
- Blank subcategory values
- Missing discount percentages
- Currency symbols embedded in numeric fields

## Output Files
When you run the script, it generates:
- retail_transactions_raw.csv
- store_locations_raw.csv

These files are saved to the output folder defined in the script.

Requirements
Python 3.x
pandas
numpy

How to Run -- 
From the project root directory type: 
python generate-retail.py

Note:
All data is fully synthetic and does not represent any real company or customers. It was created solely for educational and portfolio purposes. 

Also keep in mind the need to possibly delete the existing CSV's to generate the data with this script. 
