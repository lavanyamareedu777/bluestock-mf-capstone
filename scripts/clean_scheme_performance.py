import pandas as pd

df = pd.read_csv(
    "data/raw/scheme_performance.csv"
)

return_cols = [
    "return_1y",
    "return_3y",
    "return_5y"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

anomalies = df[
    (df["expense_ratio"] < 0.1) |
    (df["expense_ratio"] > 2.5)
]

print("Expense Ratio Anomalies")
print(anomalies)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned successfully!")