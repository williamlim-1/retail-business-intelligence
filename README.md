# Retail Business Intelligence & Sales Analytics

Business Intelligence project analyzing **250,000+ retail transactions** to evaluate revenue, profitability, promotions, and regional performance using dimensional modeling for a simulated retail enterprise.

This project transforms raw point-of-sale data into a structured analytical model and interactive executive dashboards.

**Note:** All datasets are **synthetically generated mock data** created solely for this project.

---

# Repository Navigation

| Resource | Location |
|--------|--------|
| Raw datasets | [raw-data](./raw-data) |
| Cleaned datasets | [cleaned-data](./cleaned-data) |
| Data generation scripts | [data-generation](./data-generation) |
| Power BI dashboard | [powerbi](./powerbi) |
| Star schema diagram | [schema-image](./schema-image) |
| Analytical findings | [key-findings](./key-findings) |

---

# Project Overview

This project simulates a real-world Business Intelligence engagement for a **60-store multi-category retail chain operating across the United States**.

The objective was to convert raw transactional data into a **clean analytical data model**, then build executive dashboards to analyze business performance across stores, regions, and product categories.

The dataset contains **250,000+ retail transactions across two years of operations.**

---

# About the Company

**Industry:** Big-box general merchandise retail  
**Regions:** West, Midwest, South, Northeast  
**Store Count:** 60  
**Product Catalog:** 1,200+ SKUs across 10 categories

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

The company operates a **promotion-driven retail model** where discount campaigns, category mix, and regional demand patterns significantly influence revenue and margin performance.

---

# Dataset Description

Two datasets simulate a real POS export environment.

### 1. retail_transactions_raw.csv

Contains **250,000+ retail transactions** with fields including:

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

Intentional **data quality issues** were introduced to simulate common enterprise export problems.

Dataset available here:  
[raw-data](./raw-data)

---

### 2. store_locations_raw.csv

Contains store-level metadata including:

- store_code  
- store_name  
- city  
- state  
- region  
- store_size  
- open_date  

---

# Data Preparation Process

Before analysis, the raw dataset required several cleaning and transformation steps:

- Timestamp normalization  
- Category naming standardization  
- Removal of currency formatting from numeric fields  
- Handling of missing discount values  
- Validation of revenue and profit calculations  

The cleaned datasets used for analysis are available in:

[cleaned-data](./cleaned-data)

---

# Data Model

A **star schema** was designed to support reporting performance and analytical flexibility.

### Fact Table

- Sales Transactions

### Dimension Tables

- Store  
- Product  
- Date  
- Customer  

The schema diagram can be viewed here:

[schema-image](./schema-image)

---

# Key Business Questions

This dashboard addresses several executive-level retail analytics questions:

- Which product categories generate the most revenue?
- Which categories deliver the highest profit margins?
- How much revenue is driven by promotional sales?
- How do promotional margins compare to non-promotional margins?
- Which regions and states generate the most revenue?
- Which individual stores outperform their regional averages?
- Which products generate the highest sales revenue?
- Do discount levels vary across product categories?

📊 **Full analytical answers and insights can be found in the detailed findings report:**

[View Key Findings](./key-findings/keyfindings.md)

---

# Key KPIs

The dashboard tracks several core retail performance metrics:

- **Total Revenue**
- **Gross Profit**
- **Profit Margin %**
- **Promotion Revenue %**
- **Non-Promotional Profit Margin %**
- **Promotional Profit Margin %**
- **Average Discount %**
- **Revenue by Category**
- **Revenue by Region / State**
- **Top Products by Revenue**
- **Store Performance vs Regional Average**

### Summary Results

- **$149.28M Total Revenue**
- **$64.37M Gross Profit**
- **43.12% Overall Profit Margin**
- **25.34% of Revenue from Promotions**
- **46.59% Non-Promotion Margin**
- **32.87% Promotion Margin**
- **7.16% Average Discount**

---

# Dashboard Features

The Power BI dashboard contains three analytical views.

### Executive Summary

Provides high-level metrics including:

- revenue
- profit
- margin performance
- promotion impact
- category revenue distribution
- monthly revenue trends

---

### Regional Performance

Analyzes geographic performance including:

- revenue by state
- revenue by region
- store performance vs regional average

---

### Category Analysis

Examines product performance including:

- profit margins by category
- discount behavior across categories
- revenue distribution by category and subcategory

Dashboard images will be here:

[powerbi](./powerbi)

---

# Tech Stack

### Data Generation and Preparation

- Python  
- pandas  

### Business Intelligence

- Power BI  
- DAX  

### Data Modeling

- Dimensional modeling  
- Star schema  

### Data Storage

- CSV datasets  

---

# Key Analytical Findings

A full written breakdown of the analytical insights is available here:

📊 **Key Findings Report**

[Read the Key Findings](./key-findings/keyfindings.md)

The findings document summarizes:

- category profitability insights  
- promotion effectiveness  
- regional sales performance  
- top products and revenue drivers  
- strategic business observations
