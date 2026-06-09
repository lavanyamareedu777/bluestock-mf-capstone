import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

txn = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

nav.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "investor_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "scheme_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully")