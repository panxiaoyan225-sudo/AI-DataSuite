# Phase 1 — Data Audit Findings

## 1. Data Grain
- **98 rows × 30 columns** loaded from MySQL `pipeline.Expense`
- **10 Reporting Months** (Jan-2026 to Oct-2026), **4 Business Units**, **12 Cost Centres**, **9 Expense Categories**, **3 Funding Types**
- **One row = Cost Centre × Reporting Month × Expense Category** (granular expense record)
- **1 duplicate** (Cost Centre, Reporting Month) combination found — requires investigation

## 2. Approved Budget Repetition
- **All 12 Cost Centres** have varying Approved Budget across rows
- Budget varies by row (by category and/or month) — NOT a single annual figure per cost centre
- Cannot determine if Approved Budget is annual or monthly from data alone — **requires human confirmation**

## 3. YTD Actual vs Monthly
- YTD Actual shows **increases across months** for same Cost Centre → **cumulative YTD**
- Cannot derive true monthly expense from YTD without knowing if values are truly cumulative

## 4. Full-Year Forecast
- **All 12 Cost Centres** have varying Full-Year Forecast (96 unique values out of 98 rows)
- Forecast varies by row — unclear if annual or per-category

## 5. Cost Centre Identification
- **Cost Centre alone uniquely identifies** a cost centre (12 unique values, no duplicates)
- Cost Centre + Description + Business Unit is fully consistent

## 6. Data Quality
- **Missing values**: Last Refresh Date (97/98 null), Legacy Tracking Field (81/98 null) — non-critical
- **Duplicates**: 0 exact duplicate rows; 1 duplicate (Cost Centre, Reporting Month)
- **Invalid values**: None (no negatives or nulls in financial columns)
- **Categories**: 9 expense categories, 3 funding types — consistent

## 7. Critical Bug: Total Expense Calculation
- Current code: `Total Expense = Salary + Consulting + Capital` only
- **Missing 6 of 9 expense categories**: Operations, Training, Travel, Technology, Consultants, Professional Services
- Categories like Operations, Training, etc. show **$0 Total Expense** despite having YTD Actual values
- **Aggregation by category is wrong** — Operations/Training/etc. all show $0

## 8. Critical Bug: Budget Variance
- Current code: `Budget Variance = YTD Actual - Approved Budget`
- If Approved Budget is annual and YTD Actual is cumulative → **apples-to-oranges comparison**
- No YTD Budget calculation exists

## 9. No Reconciliation Checks
- No verification that totals reconcile across Business Unit, Category, Cost Centre, Funding Type
- No validation of variance or percentage calculations

## 10. Clustering on Incorrect Data
- KMeans uses Total Expense which is wrong (missing 6 categories)
- Cluster profiles are therefore unreliable