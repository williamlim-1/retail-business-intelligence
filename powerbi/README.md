# Sales Dashboard

This directory contains the **Power BI dashboard** developed for the Retail Business Intelligence & Sales Analytics project. The dashboard visualizes key performance metrics derived from the simulated retail dataset and provides an interactive interface for exploring revenue, profitability, promotions, and regional performance.

---

# Dashboard Overview

The dashboard was designed to simulate a **real-world executive reporting environment** for a multi-location retail business. It allows users to explore performance across multiple dimensions including time, geography, product category, and promotional activity.

The dashboard is organized into three primary analytical views:

### Executive Summary
Provides a high-level overview of overall company performance, including:

- Total Revenue
- Gross Profit
- Profit Margin %
- Promotion Revenue %
- Non-Promotional Profit Margin %
- Promotional Profit Margin %
- Monthly Revenue Trends
- Revenue by Product Category
- Top Revenue-Generating Products

This page is intended to give leadership a quick understanding of the company’s overall financial performance.

---

### Regional Performance

This page focuses on geographic performance across the retail network.

Key elements include:

- Revenue by State
- Revenue per Store by Region
- Store Performance vs Regional Average
- Store-level revenue and margin comparison

These visualizations help identify **high-performing regions and stores**, as well as locations that outperform their regional benchmarks.

---

### Category Analysis

This section examines how different product categories contribute to revenue and profitability.

Visualizations include:

- Profit Margin by Category
- Average Discount by Category
- Revenue by Category and Subcategory

This page highlights differences in **category-level profitability, discount behavior, and revenue distribution** across the product catalog.

---

# Data Source

The data used in this dashboard is **not real company data**.

All datasets used in this project were **synthetically generated** using Python scripts for the purpose of building a realistic Business Intelligence portfolio project. The generated dataset simulates a retail POS system with:

- 250,000+ transactions  
- 60 store locations  
- 1,200+ products  
- Multiple product categories and subcategories  
- Promotional and non-promotional sales  

No proprietary or real business data is included in this repository.

---

# PDF Export Note

A PDF version of the dashboard is included for quick viewing.

When exporting the dashboard to PDF, the **Category Analysis page did not fully scale to the page size**, which caused some visual elements to appear slightly compressed or partially cut off in the export.

The dashboard itself renders correctly when viewed directly within **Power BI Desktop**, where all visuals display as intended.

---

# Tools Used

- **Power BI Desktop** — dashboard development and visualization
- **DAX** — KPI and measure calculations
- **Python (pandas)** — data generation and preparation
- **Dimensional modeling (Star Schema)** — analytical data structure

---

# Purpose of This Dashboard

This dashboard was created as part of a **portfolio Business Intelligence project** to demonstrate skills in:

- data modeling
- KPI design
- retail performance analysis
- interactive dashboard development
- translating raw transactional data into business insights

The project simulates the type of analysis commonly performed in **retail analytics, BI consulting, and data analytics roles**.
