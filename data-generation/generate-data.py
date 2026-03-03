import os
import numpy as np
import pandas as pd
from datetime import date, timedelta

# ──────────────────────────────────────────────
# 0.  CONFIG & SEED
# ──────────────────────────────────────────────
SEED        = 42
N_TX        = 250_000
N_STORES    = 60
N_PRODUCTS  = 1_200
N_CUSTOMERS = 25_000
START_DATE  = date(2023, 1, 1)
END_DATE    = date(2024, 12, 31)
OUT_DIR     = "raw-data"

rng = np.random.default_rng(SEED)
os.makedirs(OUT_DIR, exist_ok=True)

# ──────────────────────────────────────────────
# 1.  STORE MASTER  (60 stores, 4 regions)
# ──────────────────────────────────────────────
regions      = ["West", "Midwest", "South", "Northeast"]
region_sizes = [15, 15, 15, 15]          # 15 stores per region

state_pool = {
    "West":      [("Los Angeles","CA"),("San Francisco","CA"),("Seattle","WA"),
                  ("Portland","OR"),("Phoenix","AZ"),("Denver","CO"),
                  ("Las Vegas","NV"),("Salt Lake City","UT"),("Boise","ID"),
                  ("Spokane","WA"),("Tucson","AZ"),("Oakland","CA"),
                  ("Sacramento","CA"),("Reno","NV"),("Albuquerque","NM")],
    "Midwest":   [("Chicago","IL"),("Columbus","OH"),("Indianapolis","IN"),
                  ("Detroit","MI"),("Minneapolis","MN"),("Kansas City","MO"),
                  ("Milwaukee","WI"),("Omaha","NE"),("Cleveland","OH"),
                  ("St. Louis","MO"),("Cincinnati","OH"),("Des Moines","IA"),
                  ("Grand Rapids","MI"),("Madison","WI"),("Wichita","KS")],
    "South":     [("Houston","TX"),("Atlanta","GA"),("Miami","FL"),
                  ("Dallas","TX"),("Charlotte","NC"),("Nashville","TN"),
                  ("Austin","TX"),("Orlando","FL"),("San Antonio","TX"),
                  ("Jacksonville","FL"),("Memphis","TN"),("Louisville","KY"),
                  ("Baltimore","MD"),("Richmond","VA"),("New Orleans","LA")],
    "Northeast": [("New York","NY"),("Philadelphia","PA"),("Boston","MA"),
                  ("Pittsburgh","PA"),("Providence","RI"),("Hartford","CT"),
                  ("Buffalo","NY"),("Albany","NY"),("Newark","NJ"),
                  ("Rochester","NY"),("Worcester","MA"),("Bridgeport","CT"),
                  ("Allentown","PA"),("Springfield","MA"),("Yonkers","NY")],
}

store_name_templates = [
    "{city} Outlet", "{city} Retail Center", "{city} Superstore",
    "{city} Market", "{city} Depot", "{city} Plaza Store",
]

store_sizes_pool = ["Small", "Medium", "Large"]
size_weights     = [0.3, 0.45, 0.25]

stores = []
store_idx = 1
for region, city_states in state_pool.items():
    for city, state in city_states:
        code  = f"S{store_idx:03d}"
        tpl   = store_name_templates[store_idx % len(store_name_templates)]
        sname = tpl.format(city=city)
        ssize = rng.choice(store_sizes_pool, p=size_weights)
        # Random open date between 2015 and 2022
        open_yr  = rng.integers(2015, 2023)
        open_mo  = rng.integers(1, 13)
        open_dy  = rng.integers(1, 28)
        open_dt  = f"{open_yr}-{open_mo:02d}-{open_dy:02d}"
        stores.append(dict(
            store_code=code, store_name=sname,
            city=city, state=state, region=region,
            store_size=ssize, open_date=open_dt
        ))
        store_idx += 1

stores_df = pd.DataFrame(stores)

# ──────────────────────────────────────────────
# 2.  PRODUCT CATALOG  (1 200 products)
# ──────────────────────────────────────────────
# (category, subcategory, base_price_range, cost_pct_range)
category_spec = [
    # cat                 subcat                  price_lo  price_hi  cost_lo cost_hi  count
    ("Electronics",       "Smartphones",           299, 1199, 0.55, 0.70,  40),
    ("Electronics",       "Laptops",               499, 2499, 0.55, 0.68,  40),
    ("Electronics",       "Tablets",               199,  899, 0.55, 0.68,  30),
    ("Electronics",       "Accessories",            9,   79,  0.40, 0.60,  50),
    ("Electronics",       "Audio",                 29,  499,  0.50, 0.65,  40),
    ("Apparel",           "Men's Clothing",         19,  149,  0.30, 0.50,  80),
    ("Apparel",           "Women's Clothing",       19,  179,  0.30, 0.50,  80),
    ("Apparel",           "Footwear",               39,  249,  0.35, 0.52,  60),
    ("Apparel",           "Sportswear",             25,  120,  0.32, 0.50,  60),
    ("Home & Garden",     "Furniture",             149, 1499,  0.50, 0.70,  50),
    ("Home & Garden",     "Kitchen",                9,  199,  0.40, 0.60,  60),
    ("Home & Garden",     "Bedding",               29,  199,  0.40, 0.58,  50),
    ("Home & Garden",     "Tools",                 12,  299,  0.45, 0.65,  50),
    ("Home & Garden",     "Outdoor",               25,  599,  0.48, 0.65,  50),
    ("Grocery",           "Beverages",              1,   25,  0.55, 0.75,  80),
    ("Grocery",           "Snacks",                 1,   15,  0.55, 0.72,  70),
    ("Grocery",           "Dairy",                  1,   12,  0.60, 0.78,  60),
    ("Grocery",           "Bakery",                 2,   20,  0.55, 0.72,  60),
    ("Health & Beauty",   "Skincare",              12,  129,  0.35, 0.55,  50),
    ("Health & Beauty",   "Hair Care",              5,   45,  0.38, 0.56,  50),
    ("Health & Beauty",   "Vitamins",               8,   59,  0.40, 0.58,  40),
    ("Sports",            "Fitness Equipment",     29,  899,  0.50, 0.68,  40),
    ("Sports",            "Outdoor Recreation",    19,  499,  0.48, 0.65,  40),
    ("Toys & Games",      "Board Games",           15,   79,  0.40, 0.58,  40),
    ("Toys & Games",      "Action Figures",         8,   59,  0.38, 0.55,  50),
    ("Office Supplies",   "Stationery",             1,   29,  0.45, 0.62,  60),
    ("Office Supplies",   "Printers & Ink",        29,  399,  0.50, 0.68,  40),
    ("Automotive",        "Car Accessories",       15,  299,  0.48, 0.65,  40),
    ("Automotive",        "Maintenance",            5,   79,  0.50, 0.68,  40),
    ("Premium",           "Luxury Watches",       299, 4999,  0.30, 0.45,  20),
    ("Premium",           "Designer Bags",        199, 2499,  0.28, 0.42,  20),
]

# Verify total count <= 1 200; we'll scale if needed
total_spec = sum(row[6] for row in category_spec)  # 1 592; clip proportionally

product_rows = []
sku_idx = 1

# Adjective pools to make unique product names
adjectives = ["Pro","Elite","Ultra","Essential","Select","Classic","Signature",
               "Deluxe","Premium","Standard","Advanced","Express","Smart","Active"]
colors = ["Black","White","Silver","Blue","Red","Green","Gray","Navy","Beige","Brown"]

for row in category_spec:
    cat, subcat, plo, phi, clo, chi, cnt = row
    # Scale count so total ~= 1 200
    cnt_scaled = max(1, round(cnt * N_PRODUCTS / total_spec))
    for _ in range(cnt_scaled):
        adj   = rng.choice(adjectives)
        col   = rng.choice(colors)
        # Derive a product name
        pname = f"{adj} {subcat.split()[0]} {col} {sku_idx % 99 + 1}"
        price = round(float(rng.uniform(plo, phi)), 2)
        cost_pct = float(rng.uniform(clo, chi))
        product_rows.append(dict(
            product_sku=f"P{sku_idx:06d}",
            product_name=pname,
            category=cat,
            subcategory=subcat,
            unit_price=price,
            cost_pct=cost_pct,
        ))
        sku_idx += 1
        if sku_idx > N_PRODUCTS:
            break
    if sku_idx > N_PRODUCTS:
        break

products_df = pd.DataFrame(product_rows).head(N_PRODUCTS).reset_index(drop=True)

# ──────────────────────────────────────────────
# 3.  CUSTOMER MASTER
# ──────────────────────────────────────────────
segments = ["Consumer", "Corporate", "Home Office"]
seg_weights = [0.60, 0.30, 0.10]
customer_ids = [f"C{i:06d}" for i in range(1, N_CUSTOMERS + 1)]
customer_segments = rng.choice(segments, size=N_CUSTOMERS, p=seg_weights)
customers_df = pd.DataFrame({"customer_id": customer_ids, "customer_segment": customer_segments})

# ──────────────────────────────────────────────
# 4.  DATE RANGE & SEASONALITY WEIGHTS
# ──────────────────────────────────────────────
all_dates = pd.date_range(START_DATE, END_DATE, freq="D")
n_days    = len(all_dates)

# Daily weight: base 1.0, Nov/Dec +60%, weekends +20%
date_weights = np.ones(n_days)
for i, d in enumerate(all_dates):
    if d.month in (11, 12):
        date_weights[i] *= 1.60
    if d.dayofweek >= 5:           # Saturday=5, Sunday=6
        date_weights[i] *= 1.20

date_weights /= date_weights.sum()

# Sample transaction dates
tx_date_indices = rng.choice(n_days, size=N_TX, p=date_weights)
tx_dates = all_dates[tx_date_indices]

# ──────────────────────────────────────────────
# 5.  BUILD TRANSACTIONS
# ──────────────────────────────────────────────

# --- Region → category affinity multipliers (simple rules) ---
# Each region prefers certain categories (higher probability weight)
region_cat_affinity = {
    "West":      {"Electronics": 1.5, "Sports": 1.4, "Health & Beauty": 1.3},
    "Midwest":   {"Grocery": 1.5, "Home & Garden": 1.4, "Automotive": 1.3},
    "South":     {"Apparel": 1.5, "Grocery": 1.4, "Automotive": 1.3},
    "Northeast": {"Premium": 1.8, "Electronics": 1.3, "Office Supplies": 1.4},
}

# Pre-build per-region product weight arrays
products_df["_idx"] = np.arange(len(products_df))
region_product_weights = {}
for region, affinity in region_cat_affinity.items():
    w = np.ones(len(products_df))
    for i, cat in enumerate(products_df["category"]):
        if cat in affinity:
            w[i] *= affinity[cat]
    w /= w.sum()
    region_product_weights[region] = w

# Sample stores and get their regions
store_indices    = rng.integers(0, N_STORES, size=N_TX)
selected_stores  = stores_df.iloc[store_indices].reset_index(drop=True)
tx_regions       = selected_stores["region"].values

# Sample products using region-aware weights (vectorised per region)
product_indices = np.empty(N_TX, dtype=int)
for region in regions:
    mask = tx_regions == region
    n    = mask.sum()
    if n > 0:
        product_indices[mask] = rng.choice(
            len(products_df), size=n, p=region_product_weights[region]
        )

selected_products = products_df.iloc[product_indices].reset_index(drop=True)

# Sample customers
cust_indices     = rng.integers(0, N_CUSTOMERS, size=N_TX)
selected_custs   = customers_df.iloc[cust_indices].reset_index(drop=True)

# Promo flag: 20% base, higher in Nov/Dec
tx_months        = tx_dates.month
base_promo_prob  = np.where(np.isin(tx_months, [11, 12]), 0.35, 0.20)
promo_flag       = (rng.random(N_TX) < base_promo_prob).astype(int)

# Qty: 1–8; promo increases mean qty slightly
qty_base = rng.integers(1, 5, size=N_TX)              # 1–4 base
qty_extra = (promo_flag * rng.integers(0, 3, size=N_TX))  # 0–2 extra for promo
qty = np.clip(qty_base + qty_extra, 1, 8)

# Discount: promo rows get higher discount probability
discount_pct = np.where(
    promo_flag == 1,
    rng.uniform(0.05, 0.40, size=N_TX),
    rng.choice([0.0, 0.0, 0.0, rng.uniform(0, 0.20)], size=N_TX)
    # ~75% chance of 0 discount without promo
)
# The choice trick above doesn't vectorise cleanly; fix:
no_promo_disc = np.where(
    rng.random(N_TX) < 0.75,
    0.0,
    rng.uniform(0.0, 0.20, size=N_TX)
)
discount_pct = np.where(promo_flag == 1, rng.uniform(0.05, 0.40, size=N_TX), no_promo_disc)
discount_pct = np.round(np.clip(discount_pct, 0.0, 0.40), 4)

unit_price  = selected_products["unit_price"].values
cost_pct    = selected_products["cost_pct"].values
unit_cost   = np.round(unit_price * cost_pct, 2)

extended_amount = np.round(qty * unit_price * (1 - discount_pct), 2)
profit          = np.round(extended_amount - qty * unit_cost, 2)

payment_types   = ["Credit", "Debit", "Cash", "Apple Pay", "Gift Card"]
pay_weights     = [0.35, 0.30, 0.15, 0.15, 0.05]
payment_type    = rng.choice(payment_types, size=N_TX, p=pay_weights)

# ──────────────────────────────────────────────
# 6.  ASSEMBLE DATAFRAME
# ──────────────────────────────────────────────
# Transaction IDs
tx_ids = [f"TXN{i:08d}" for i in range(1, N_TX + 1)]

# Timestamps: mix of two formats (~15% use the messy format)
def build_timestamps(dates, n, rng):
    hours   = rng.integers(7, 22, size=n)
    minutes = rng.integers(0, 60, size=n)
    seconds = rng.integers(0, 60, size=n)
    use_alt = rng.random(n) < 0.15     # 15% messy format
    timestamps = []
    for i in range(n):
        d  = dates[i]
        h, m, s = int(hours[i]), int(minutes[i]), int(seconds[i])
        if use_alt[i]:
            # "MM/DD/YYYY H:MM AM/PM"
            period = "AM" if h < 12 else "PM"
            h12    = h % 12 or 12
            ts = f"{d.month:02d}/{d.day:02d}/{d.year} {h12}:{m:02d} {period}"
        else:
            ts = f"{d.year}-{d.month:02d}-{d.day:02d} {h:02d}:{m:02d}:{s:02d}"
        timestamps.append(ts)
    return timestamps

timestamps = build_timestamps(tx_dates, N_TX, rng)

df = pd.DataFrame({
    "transaction_id":    tx_ids,
    "transaction_ts":    timestamps,
    "store_code":        selected_stores["store_code"].values,
    "store_name":        selected_stores["store_name"].values,
    "region":            selected_stores["region"].values,
    "product_sku":       selected_products["product_sku"].values,
    "product_name":      selected_products["product_name"].values,
    "category":          selected_products["category"].values,
    "subcategory":       selected_products["subcategory"].values,
    "customer_id":       selected_custs["customer_id"].values,
    "customer_segment":  selected_custs["customer_segment"].values,
    "payment_type":      payment_type,
    "qty":               qty,
    "unit_price":        unit_price,
    "discount_pct":      discount_pct,
    "promo_flag":        promo_flag,
    "extended_amount":   extended_amount,
    "unit_cost":         unit_cost,
    "profit":            profit,
})

# ──────────────────────────────────────────────
# 7.  INJECT DATA QUALITY ISSUES
# ──────────────────────────────────────────────

# 7a. Category casing/spacing variations (~3%)
cat_noise_idx = rng.choice(N_TX, size=int(N_TX * 0.03), replace=False)
cat_variants  = {
    "Electronics":   ["electronics ", "ELECTRONICS", "Electronics"],
    "Apparel":       ["apparel", "APPAREL", "Apparel"],
    "Grocery":       ["grocery", "GROCERY", "Grocery"],
    "Home & Garden": ["Home & garden", "home & garden", "HOME & GARDEN"],
    "Health & Beauty":["health & beauty", "Health & Beauty ", "HEALTH & BEAUTY"],
    "Sports":        ["sports", "SPORTS", "Sports"],
    "Premium":       ["premium", "PREMIUM", "Premium"],
    "Toys & Games":  ["toys & games", "Toys & games", "TOYS & GAMES"],
    "Office Supplies":["office supplies", "OFFICE SUPPLIES", "Office Supplies "],
    "Automotive":    ["automotive", "AUTOMOTIVE", "Automotive"],
}
for idx in cat_noise_idx:
    orig = df.at[idx, "category"]
    variants = cat_variants.get(orig, [orig.lower(), orig.upper()])
    df.at[idx, "category"] = rng.choice(variants)

# 7b. Store name aliases (~2%)
# Build a per-store alias map (one alternate name per store)
alias_map = {}
for _, row in stores_df.iterrows():
    name = row["store_name"]
    # Swap "Outlet" → "Store Outlet", insert space in city, etc.
    alt = name.replace("Outlet", "Store Outlet").replace("Center", "Centre")
    if alt == name:
        parts = name.split()
        if len(parts) >= 2:
            alt = parts[0] + " " + parts[0][0] + ". " + " ".join(parts[1:])
    alias_map[row["store_code"]] = alt

store_alias_idx = rng.choice(N_TX, size=int(N_TX * 0.02), replace=False)
for idx in store_alias_idx:
    sc = df.at[idx, "store_code"]
    df.at[idx, "store_name"] = alias_map.get(sc, df.at[idx, "store_name"])

# 7c. Blank subcategory (~1%)
blank_sub_idx = rng.choice(N_TX, size=int(N_TX * 0.01), replace=False)
df.loc[blank_sub_idx, "subcategory"] = ""

# 7d. Missing discount_pct (~1%)
miss_disc_idx = rng.choice(N_TX, size=int(N_TX * 0.01), replace=False)
df.loc[miss_disc_idx, "discount_pct"] = np.nan

# 7e. unit_price as string with "$" (~0.5%)
price_str_idx = rng.choice(N_TX, size=int(N_TX * 0.005), replace=False)
df["unit_price"] = df["unit_price"].astype(object)
for idx in price_str_idx:
    df.at[idx, "unit_price"] = f"${df.at[idx, 'unit_price']}"

# ──────────────────────────────────────────────
# 8. EXPORT
# ──────────────────────────────────────────────

tx_path = os.path.join(OUT_DIR, "retail_transactions_raw.csv")
store_path = os.path.join(OUT_DIR, "store_locations_raw.csv")

# Prevent accidental overwrite of committed repo files
if os.path.exists(tx_path) or os.path.exists(store_path):
    print("Output files already exist in raw-data/.")
    print("Delete them manually if you want to regenerate full datasets.")
else:
    df.to_csv(tx_path, index=False)
    stores_df.to_csv(store_path, index=False)
    print("Data generation complete.")
    print(f"Transactions file saved to: {tx_path}")
    print(f"Store master file saved to: {store_path}")

print("Data generation complete.")
print(f"Transactions file saved to: {tx_path}")
print(f"Store master file saved to: {store_path}")
