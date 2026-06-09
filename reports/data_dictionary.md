# Data Dictionary

## nav_history

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique fund identifier |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value |

## investor_transactions

| Column | Data Type | Description |
|----------|----------|----------|
| transaction_id | INTEGER | Unique transaction |
| amount | FLOAT | Investment amount |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |

## scheme_performance

| Column | Data Type | Description |
|----------|----------|----------|
| return_1y | FLOAT | One year return |
| return_3y | FLOAT | Three year CAGR |
| return_5y | FLOAT | Five year CAGR |
| expense_ratio | FLOAT | Annual expense ratio |