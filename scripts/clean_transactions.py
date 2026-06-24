import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date column
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Remove duplicates
df = df.drop_duplicates()

# Keep only positive transaction amounts
df = df[df["amount_inr"] > 0]

# Standardize transaction types
df["transaction_type"] = df["transaction_type"].str.strip().str.title()

# Standardize KYC status
df["kyc_status"] = df["kyc_status"].str.strip().str.title()

print("\nUnique Transaction Types:")
print(df["transaction_type"].unique())

print("\nUnique KYC Status:")
print(df["kyc_status"].unique())

print("\nRows after cleaning:", len(df))

# Save cleaned file
df.to_csv("data/processed/08_investor_transactions_cleaned.csv", index=False)

print("\nSaved Successfully!")
