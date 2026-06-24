# Data Dictionary

## fact_nav

| Column    | Type    | Description             |
| --------- | ------- | ----------------------- |
| amfi_code | INTEGER | Unique AMFI scheme code |
| date      | DATE    | NAV date                |
| nav       | REAL    | Net Asset Value         |

---

## fact_transactions

| Column             | Type    | Description                    |
| ------------------ | ------- | ------------------------------ |
| investor_id        | TEXT    | Unique investor identifier     |
| transaction_date   | DATE    | Transaction date               |
| amfi_code          | INTEGER | Mutual fund scheme code        |
| transaction_type   | TEXT    | SIP, Lumpsum, Redemption       |
| amount_inr         | REAL    | Transaction amount in INR      |
| state              | TEXT    | Investor state                 |
| city               | TEXT    | Investor city                  |
| city_tier          | TEXT    | Tier classification            |
| age_group          | TEXT    | Investor age group             |
| gender             | TEXT    | Investor gender                |
| annual_income_lakh | REAL    | Annual income in lakhs         |
| payment_mode       | TEXT    | UPI, Cheque, Net Banking, etc. |
| kyc_status         | TEXT    | Verified or Pending            |

---

## fact_performance

| Column             | Type    | Description                     |
| ------------------ | ------- | ------------------------------- |
| amfi_code          | INTEGER | Scheme AMFI code                |
| scheme_name        | TEXT    | Scheme name                     |
| fund_house         | TEXT    | Fund house                      |
| category           | TEXT    | Scheme category                 |
| plan               | TEXT    | Direct or Regular               |
| return_1yr_pct     | REAL    | 1 year return percentage        |
| return_3yr_pct     | REAL    | 3 year return percentage        |
| return_5yr_pct     | REAL    | 5 year return percentage        |
| benchmark_3yr_pct  | REAL    | Benchmark return                |
| alpha              | REAL    | Alpha metric                    |
| beta               | REAL    | Beta metric                     |
| sharpe_ratio       | REAL    | Sharpe ratio                    |
| sortino_ratio      | REAL    | Sortino ratio                   |
| std_dev_ann_pct    | REAL    | Annualized standard deviation   |
| max_drawdown_pct   | REAL    | Maximum drawdown                |
| aum_crore          | REAL    | Assets under management (crore) |
| expense_ratio_pct  | REAL    | Expense ratio percentage        |
| morningstar_rating | INTEGER | Morningstar rating              |
| risk_grade         | TEXT    | Risk classification             |
