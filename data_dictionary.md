# Data Dictionary

## fact_nav

| Column | Type | Description | Source |
|--------|------|-------------|--------|
| amfi_code | INTEGER | Unique AMFI scheme code | 02_nav_history.csv |
| date | DATE | NAV date | 02_nav_history.csv |
| nav | REAL | Net Asset Value | 02_nav_history.csv |

---

## fact_transactions

| Column | Type | Description | Source |
|--------|------|-------------|--------|
| investor_id | TEXT | Unique investor identifier | 08_investor_transactions.csv |
| transaction_date | DATE | Transaction date | 08_investor_transactions.csv |
| amfi_code | INTEGER | Mutual fund scheme code | 08_investor_transactions.csv |
| transaction_type | TEXT | SIP, Lumpsum, Redemption | 08_investor_transactions.csv |
| amount_inr | REAL | Transaction amount in INR | 08_investor_transactions.csv |
| state | TEXT | Investor state | 08_investor_transactions.csv |
| city | TEXT | Investor city | 08_investor_transactions.csv |
| city_tier | TEXT | Tier classification | 08_investor_transactions.csv |
| age_group | TEXT | Investor age group | 08_investor_transactions.csv |
| gender | TEXT | Investor gender | 08_investor_transactions.csv |
| annual_income_lakh | REAL | Annual income in lakhs | 08_investor_transactions.csv |
| payment_mode | TEXT | UPI, Cheque, Net Banking, etc. | 08_investor_transactions.csv |
| kyc_status | TEXT | Verified or Pending | 08_investor_transactions.csv |

---

## fact_performance

| Column | Type | Description | Source |
|--------|------|-------------|--------|
| amfi_code | INTEGER | Scheme AMFI code | 07_scheme_performance.csv |
| scheme_name | TEXT | Scheme name | 07_scheme_performance.csv |
| fund_house | TEXT | Fund house | 07_scheme_performance.csv |
| category | TEXT | Scheme category | 07_scheme_performance.csv |
| plan | TEXT | Direct or Regular | 07_scheme_performance.csv |
| return_1yr_pct | REAL | 1 year return percentage | 07_scheme_performance.csv |
| return_3yr_pct | REAL | 3 year return percentage | 07_scheme_performance.csv |
| return_5yr_pct | REAL | 5 year return percentage | 07_scheme_performance.csv |
| benchmark_3yr_pct | REAL | Benchmark return | 07_scheme_performance.csv |
| alpha | REAL | Alpha metric | 07_scheme_performance.csv |
| beta | REAL | Beta metric | 07_scheme_performance.csv |
| sharpe_ratio | REAL | Sharpe ratio | 07_scheme_performance.csv |
| sortino_ratio | REAL | Sortino ratio | 07_scheme_performance.csv |
| std_dev_ann_pct | REAL | Annualized standard deviation | 07_scheme_performance.csv |
| max_drawdown_pct | REAL | Maximum drawdown | 07_scheme_performance.csv |
| aum_crore | REAL | Assets under Management (Crore) | 07_scheme_performance.csv |
| expense_ratio_pct | REAL | Expense ratio percentage | 07_scheme_performance.csv |
| morningstar_rating | INTEGER | Morningstar rating | 07_scheme_performance.csv |
| risk_grade | TEXT | Risk classification | 07_scheme_performance.csv |