-- ==========================================
-- Mutual Fund Analytics - Analytical Queries
-- ==========================================

-- 1. Top 5 Funds by AUM
SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Month
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. Funds with Expense Ratio below 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 4. Top 5 Funds by Sharpe Ratio
SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- 5. Transaction Count by State
SELECT
    state,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;


-- 6. SIP Year-over-Year (YoY) Growth
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE UPPER(transaction_type) = 'SIP'
GROUP BY year
ORDER BY year;


-- 7. Transaction Count by Type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;


-- 8. Average NAV
SELECT
    AVG(nav) AS average_nav
FROM fact_nav;


-- 9. Top 5 Highest NAV Values
SELECT
    amfi_code,
    date,
    nav
FROM fact_nav
ORDER BY nav DESC
LIMIT 5;


-- 10. KYC Status Distribution
SELECT
    kyc_status,
    COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY kyc_status
ORDER BY investor_count DESC;