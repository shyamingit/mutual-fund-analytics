import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Remove duplicates
df = df.drop_duplicates()

# Validate expense ratio range
anomalies = df[(df["expense_ratio_pct"] < 0.1) | (df["expense_ratio_pct"] > 2.5)]

print("\nExpense Ratio Anomalies:")
print(anomalies)

# Ensure numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nRows after cleaning:", len(df))

# Save cleaned file
df.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)

print("\nSaved Successfully!")
