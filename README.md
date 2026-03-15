# Retail Business Intelligence & Sales Analytics
End-to-end Business Intelligence project analyzing 250,000+ retail transactions to evaluate revenue, margin, promotions, and regional performance using dimensional modeling for a mock commerce/retail company. This project utilizes **MOCK DATA** generated for the sole purpose of this project. 

## Project Overview

This project simulates a real-world Business Intelligence engagement for a 60-store multi-category retail chain operating across the United States.

The objective was to transform raw POS transactional data into a structured analytical model, then build executive dashboards to evaluate:

- Revenue and profit performance  
- Promotion effectiveness  
- Regional demand differences  
- Category margin behavior  
- Data quality inconsistencies  

The dataset contains over 250,000 retail transactions across 2 years of operations.

---

## About the Company

**Industry:** Big-box general merchandise retail  
**Regions:** West, Midwest, South, Northeast  
**Store Count:** 60  
**Product Catalog:** 1,200+ SKUs across 10+ categories  

### Core Product Categories

- Electronics  
- Apparel  
- Home & Garden  
- Grocery  
- Health & Beauty  
- Sports  
- Toys & Games  
- Office Supplies  
- Automotive  
- Premium Goods  

This company operates a high-volume, promotion-driven retail model with regional category preferences and seasonal demand shifts.

---

## Dataset Description

Two raw datasets were generated to simulate a real POS export:

### 1. retail_transactions_raw.csv

Contains 250,000+ transactions with the following fields:

- transaction_id  
- transaction_ts 
- store_code  
- store_name  
- region  
- product_sku  
- product_name  
- category 
- subcategory 
- customer_id  
- customer_segment  
- payment_type  
- qty  
- unit_price 
- discount_pct 
- promo_flag  
- extended_amount  
- unit_cost  
- profit  

Controlled data quality issues were intentionally injected to simulate real enterprise exports.

### 2. store_locations_raw.csv

Contains store-level metadata:

- store_code  
- store_name  
- city  
- state  
- region  
- store_size  
- open_date  

---

## Business Questions Addressed

This project answers key executive questions:

- Which categories drive the highest revenue and margin?  
- How do promotions impact profitability?  
- Which regions over-discount?  
- Where are premium goods outperforming?  
- How does seasonality affect revenue trends?  
- Which stores are underperforming relative to region averages?  

---

## Data Preparation Process

The raw dataset required:

- Timestamp normalization  
- Category casing standardization  
- Removal of currency symbols from numeric fields  
- Handling of missing discount values  
- Validation of revenue and profit calculations  

After cleaning, the data was modeled into a structured analytical format suitable for BI reporting.

---


## Key KPIs Built

- Total Revenue  
- Gross Profit  
- Profit Margin %  
- Revenue by Region  
- Revenue by Category  
- Promotion Revenue %  
- Average Discount %  
- Units per Transaction  
- Regional Premium Penetration (Percentage of total revenue that consists of Premium Goods sales)


---

## Tech Stack

- Python (pandas)  
- CSV data generation  
- Power BI
- DAX
- Dimensional modeling (star schema)  
