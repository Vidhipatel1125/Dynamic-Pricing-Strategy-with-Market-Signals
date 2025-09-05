# src/make_data.py
import numpy as np
import pandas as pd

# random generator (so results repeat)
rng = np.random.default_rng(42)

# 1) Dates (60 days) and product categories
dates = pd.date_range("2024-01-01", periods=60, freq="D")
categories = ["oat_milk", "almond_milk", "kombucha", "protein_shake"]

# 2) Price ranges per product (in USD)
price_ranges = {
    "oat_milk": (3.5, 6.0),
    "almond_milk": (3.0, 5.0),
    "kombucha": (2.5, 5.0),
    "protein_shake": (2.0, 4.5),
}

# 3) Create an empty list to hold all the rows
rows = []

# 4) Loop over each product and each day
for cat in categories:
    base_price = rng.uniform(*price_ranges[cat])  # starting price

    for d in dates:
        # --- Promotions ---
        on_promo = rng.random() < 0.15  # 15% chance of promotion
        discount = rng.uniform(0.05, 0.15) if on_promo else 0.0
        our_price = round(base_price * (1 - discount), 2)

        # --- Competitors ---
        is_weekend = d.dayofweek in (5, 6)
        discounter_bias = rng.normal(-0.10, 0.02) + (-0.02 if is_weekend else 0.0)
        premium_bias   = rng.normal(0.15, 0.03) + (-0.01 if is_weekend else 0.0)
        discounter_price = round(max(0.5, our_price * (1 + discounter_bias)), 2)
        premium_price   = round(max(0.5, our_price * (1 + premium_bias)), 2)

        # --- Demand (units sold) ---
        price_index = our_price / base_price
        base_demand = {
            "oat_milk": 50,
            "almond_milk": 45,
            "kombucha": 35,
            "protein_shake": 40,
        }[cat]
        mean_units = base_demand * (price_index ** -0.9)
        noise = rng.normal(0, 3)
        units_sold = int(max(0, round(mean_units + noise)))

        # --- Add a row ---
        rows.append({
            "date": d,
            "category": cat,
            "our_price": our_price,
            "on_promo": int(on_promo),
            "discounter_price": discounter_price,
            "premium_price": premium_price,
            "units_sold": units_sold,
        })

# 5) Convert all rows into a DataFrame
df = pd.DataFrame(rows)

# 6) Save to CSV in the data folder
df.to_csv("data/sales_with_competitors.csv", index=False)
print("✅ Wrote data/sales_with_competitors.csv with", len(df), "rows")
