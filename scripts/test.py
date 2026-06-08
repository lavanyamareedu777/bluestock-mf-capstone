import pandas as pd

df = pd.read_csv("data/raw/fund_master.csv")

print(df.isnull().sum())