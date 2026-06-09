-- 1 Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 3 Monthly NAV
SELECT strftime('%Y-%m',date),
AVG(nav)
FROM fact_nav
GROUP BY strftime('%Y-%m',date);

-- 4 Transaction count
SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 5 Total investment
SELECT SUM(amount)
FROM fact_transactions;

-- 6 Expense ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- 7 Best 1Y returns
SELECT *
FROM fact_performance
ORDER BY return_1y DESC;

-- 8 Best 3Y returns
SELECT *
FROM fact_performance
ORDER BY return_3y DESC;

-- 9 Best 5Y returns
SELECT *
FROM fact_performance
ORDER BY return_5y DESC;

-- 10 Transactions by state
SELECT state,
COUNT(*)
FROM investor_transactions
GROUP BY state;