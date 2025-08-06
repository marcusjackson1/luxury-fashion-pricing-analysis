import pandas as pd
import sqlite3
import os

RAW_SSENSE_PATH = '/Users/marcusjackson/Desktop/DS/luxury-fashion-pricing-analysis/data/raw/ssense_data.csv'
RAW_TRENDS_PATH = '/Users/marcusjackson/Desktop/DS/luxury-fashion-pricing-analysis/data/raw/google_trends_real.csv'
CLEANED_CSV_PATH = '/Users/marcusjackson/Desktop/DS/luxury-fashion-pricing-analysis/data/processed/cleaned_data.csv'
SQLITE_DB_PATH = '/Users/marcusjackson/Desktop/DS/luxury-fashion-pricing-analysis/data/processed/database.db'

# 1. Load data
ssense_df = pd.read_csv(RAW_SSENSE_PATH)
trends_df = pd.read_csv(RAW_TRENDS_PATH)

# 2. Clean SSENSE data
ssense_df['price'] = ssense_df['price_usd'].replace('[\$,]', '', regex=True).astype(float)
ssense_df['brand'] = ssense_df['brand'].str.lower().str.strip()

# 3. Clean Google Trends data
trends_df_long = trends_df.melt(var_name='brand', value_name='brand_popularity')
trends_df_long['brand'] = trends_df_long['brand'].str.lower().str.strip()
date_range = pd.date_range(start='2023-01-01', periods=len(trends_df), freq='W')
num_brands = trends_df.shape[1]
trends_df_long['date'] = list(date_range) * num_brands

# 4. Merge datasets
merged_df = pd.merge(ssense_df, trends_df_long, on='brand', how='left')

# 5. Save cleaned CSV
os.makedirs("data/processed", exist_ok=True)
merged_df.to_csv(CLEANED_CSV_PATH, index=False)

# 6. Save to SQLite
conn = sqlite3.connect(SQLITE_DB_PATH)
merged_df.to_sql("fashion_data", conn, if_exists="replace", index=False)
conn.close()

print("Data cleaning complete. Cleaned CSV and DB created.")
