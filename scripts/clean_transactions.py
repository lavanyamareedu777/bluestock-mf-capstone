import pandas as pd

# Load data
df = pd.read_csv("data/raw/investor_transactions.csv")

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
      .astype(str)
      .str.strip()
      .str.title()
)

# Amount validation
df = df[df["amount"] > 0]

# Valid KYC values
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC Records:", len(invalid_kyc))

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned successfully!")