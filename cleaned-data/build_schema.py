import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "raw-data"))
OUT_DIR = BASE_DIR


# NOTE: Repository includes sample raw data due to file size limits.
# Full dataset used during development is not automatically included but can be generated.
TX_FILE = "retail_transactions_raw.csv"
STORE_FILE = "store_locations_raw.csv"

tx_path = os.path.join(RAW_DIR, TX_FILE)
store_path = os.path.join(RAW_DIR, STORE_FILE)

print("TX path:", tx_path)
print("Store path:", store_path)

df_tx = pd.read_csv(tx_path)
df_store = pd.read_csv(store_path)


def clean_tx(df):
    # 1) Parse timestamps (mixed formats)
    df["transaction_dt"] = pd.to_datetime(df["transaction_ts"], errors="coerce")

     # Second pass: only fix the ones that failed (AM/PM format)
    mask = df["transaction_dt"].isna()
    df.loc[mask, "transaction_dt"] = pd.to_datetime(
        df.loc[mask, "transaction_ts"],
        format="%m/%d/%Y %I:%M %p",
        errors="coerce"
    )

    # 2) Create date_key
    df["date_key"] = df["transaction_dt"].dt.strftime("%Y%m%d").astype("Int64")

    # 3) Clean unit_price (remove $) and convert to numeric
    df["unit_price"] = df["unit_price"].astype(str).str.replace("$", "", regex=False)
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    # 4) Clean discount_pct (fill missing with 0)
    df["discount_pct"] = pd.to_numeric(df["discount_pct"], errors="coerce").fillna(0.0)

    # 5) Ensure qty is numeric
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")

    # 6) Recalculate revenue and profit (consistent math)
    df["extended_amount"] = df["qty"] * df["unit_price"] * (1 - df["discount_pct"])
    df["profit"] = df["extended_amount"] - (df["qty"] * df["unit_cost"])

    # 7) Standardize category / subcategory for DimProduct
    df["category"] = df["category"].astype(str).str.strip().str.title()
    df["subcategory"] = df["subcategory"].fillna("").astype(str).str.strip()
    df.loc[df["subcategory"] == "", "subcategory"] = "Unknown"

    return df

def clean_store(df):
   # convert open date to datetime
   df['open_date'] = pd.to_datetime(df['open_date'], errors='coerce')
   return df

df_store = clean_store(df_store)
df_tx = clean_tx(df_tx)

def create_dimdate(df_tx):
    min_date = df_tx["transaction_dt"].min().date()
    max_date = df_tx["transaction_dt"].max().date()

    dates = pd.date_range(min_date, max_date, freq="D")

    dim_date = pd.DataFrame({"full_date": dates})
    dim_date["date_key"] = dim_date["full_date"].dt.strftime("%Y%m%d").astype(int)
    dim_date["year"] = dim_date["full_date"].dt.year
    dim_date["quarter"] = dim_date["full_date"].dt.quarter
    dim_date["month_number"] = dim_date["full_date"].dt.month
    dim_date["month_name"] = dim_date["full_date"].dt.strftime("%B")
    dim_date["month_year"] = dim_date["full_date"].dt.strftime("%Y-%m")
    dim_date["day_of_week_number"] = dim_date["full_date"].dt.dayofweek + 1
    dim_date["day_name"] = dim_date["full_date"].dt.strftime("%A")
    dim_date["is_weekend"] = dim_date["day_of_week_number"].isin([6, 7]).astype(int)

    return dim_date


def create_dim_tables(df_tx, df_store):
    # Fact table
    fact_table = df_tx[[
        "transaction_id",
        "date_key",
        "store_code",
        "product_sku",
        "customer_id",
        "payment_type",
        "qty",
        "unit_price",
        "discount_pct",
        "promo_flag",
        "extended_amount",
        "unit_cost",
        "profit",
    ]].copy()

    # Dimensions
    dim_store = df_store.drop_duplicates(subset=["store_code"]).copy()

    dim_product = df_tx[[
        "product_sku", "product_name", "category", "subcategory"
    ]].drop_duplicates(subset=["product_sku"]).copy()

    dim_customer = df_tx[[
        "customer_id", "customer_segment"
    ]].drop_duplicates(subset=["customer_id"]).copy()

    dim_date = create_dimdate(df_tx)

    return fact_table, dim_store, dim_product, dim_customer, dim_date


# Build tables
fact_table, dim_store, dim_product, dim_customer, dim_date = create_dim_tables(df_tx, df_store)

# Export
fact_table.to_csv(os.path.join(OUT_DIR, "fact_sales.csv"), index=False)
dim_store.to_csv(os.path.join(OUT_DIR, "dim_store.csv"), index=False)
dim_product.to_csv(os.path.join(OUT_DIR, "dim_product.csv"), index=False)
dim_customer.to_csv(os.path.join(OUT_DIR, "dim_customer.csv"), index=False)
dim_date.to_csv(os.path.join(OUT_DIR, "dim_date.csv"), index=False)

print("Export complete: cleaned-data/*.csv")