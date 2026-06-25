import pandas as pd
from sqlalchemy import create_engine, text

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav_df = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
txn_df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
perf_df = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Load into SQLite
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)

txn_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)

perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("\nDatabase Created Successfully!")

# --------------------------
# Verify Row Counts
# --------------------------

with engine.connect() as conn:
    nav_count = conn.execute(text("SELECT COUNT(*) FROM fact_nav")).scalar()

    txn_count = conn.execute(text("SELECT COUNT(*) FROM fact_transactions")).scalar()

    perf_count = conn.execute(text("SELECT COUNT(*) FROM fact_performance")).scalar()

print("\nRow Count Verification")
print("-" * 30)

print(f"NAV CSV Rows           : {len(nav_df)}")
print(f"NAV Database Rows      : {nav_count}")

print()

print(f"Transaction CSV Rows   : {len(txn_df)}")
print(f"Transaction DB Rows    : {txn_count}")

print()

print(f"Performance CSV Rows   : {len(perf_df)}")
print(f"Performance DB Rows    : {perf_count}")

if len(nav_df) == nav_count and len(txn_df) == txn_count and len(perf_df) == perf_count:
    print("\n✅ Row count verification PASSED.")
else:
    print("\n❌ Row count verification FAILED.")
