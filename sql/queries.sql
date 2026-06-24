-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average 1 Year Return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 3. Funds with Expense Ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 4. Highest Sharpe Ratio
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 5. Transaction Count by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 6. Total Investment Amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- 7. Transaction Count by Type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 9. Top 5 NAV Values
SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 5;

-- 10. KYC Status Distribution
SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;