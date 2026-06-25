import pandas as pd
import os

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

datasets = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
]

for file in datasets:
    path = os.path.join(RAW_DIR, file)

    df = pd.read_csv(path)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Trim whitespace in text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    output = os.path.join(PROCESSED_DIR, file.replace(".csv", "_cleaned.csv"))

    df.to_csv(output, index=False)

    print(f"Saved {output}")

print("\nAll remaining datasets processed successfully!")
