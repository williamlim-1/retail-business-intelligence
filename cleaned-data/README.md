# Cleaned Data

This folder contains the cleaned and structured data used for the Power BI dashboard.

The script `build_schema.py` reads the raw CSV files from the `raw-data` folder, applies transformation logic, and outputs a complete star schema into this directory.

> **IMPORTANT**  
> The repository includes a **sample transactions dataset** due to file size constraints.  
> By default, `build_schema.py` processes `raw-data/retail_transactions_sample.csv`.  
>  
> If you would like to run the cleaning process on the full dataset locally, update the `TX_FILE` variable in `build_schema.py` to:
>
> `retail_transactions_raw.csv`

---

## What the Script Does

- Parses mixed-format timestamps into proper datetime values  
- Creates a `date_key` column in `YYYYMMDD` format  
- Cleans `unit_price` values and converts them to numeric  
- Fills missing `discount_pct` values with `0`  
- Recalculates `extended_amount` and `profit` for consistency  
- Standardizes `category` and `subcategory` values  
- Converts store `open_date` to datetime  
- Builds structured fact and dimension tables  

---

## Output Tables

Running the script generates the following files in this folder:

- `fact_sales.csv`
- `dim_store.csv`
- `dim_product.csv`
- `dim_customer.csv`
- `dim_date.csv`

These tables form a complete **star schema** and are ready to be imported into Power BI.

---

## Data Integrity

- Raw data files remain unchanged in the `raw-data` folder.  
- All reporting and analysis should use the structured outputs in this directory.