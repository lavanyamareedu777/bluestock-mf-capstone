import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 80)
    print(f"FILE: {file}")

    file_path = os.path.join(DATA_PATH, file)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except pd.errors.EmptyDataError:
        print(f"{file} is empty. Skipping...")

    except Exception as e:
        print(f"Error reading {file}: {e}")

    print("=" * 80)