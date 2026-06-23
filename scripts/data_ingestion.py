import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw")

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

for file in csv_files:
    print("\n" + "=" * 50)
    print("FILE:", file)

    filepath = os.path.join(DATA_PATH, file)

    df = pd.read_csv(filepath)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())
