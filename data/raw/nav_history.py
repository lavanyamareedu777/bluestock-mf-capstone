import pandas as pd

df = pd.read_csv("data/raw/nav_history.csv")

# Date conversion
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV within each fund
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Keep only positive NAV values
df = df[df["nav"] > 0]

# Check nulls
print(df.isnull().sum())

df.to_csv("data/processed/nav_history_clean.csv", index=False)