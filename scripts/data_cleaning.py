import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Keep only valid NAV values
df = df[df["nav"] > 0]

# Dataset summary
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

print("\nRows after cleaning:", len(df))

# Save cleaned file
df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print("\nSaved cleaned file successfully!")
print("Location: data/processed/02_nav_history_cleaned.csv")
