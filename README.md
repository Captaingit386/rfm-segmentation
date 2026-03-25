# RFM Customer Segmentation (PostgreSQL + Python + Power BI)

## Overview
This project segments customers using the **RFM framework**:
- **Recency**: days since last purchase  
- **Frequency**: number of unique purchases (invoices)  
- **Monetary**: total revenue contributed  

It produces actionable customer groups (VIP/Champions, Loyal/Regular, New Customers, At-Risk, Lost) and a Power BI dashboard for quick business insight.

---

## Dataset
**Online Retail (2010–2011)** transactional dataset.

Key fields used:
- `CustomerID`, `InvoiceNo`, `InvoiceDate`
- `Quantity`, `UnitPrice`
- Revenue computed as: `Quantity × UnitPrice`

---

## Method
### 1) Data Cleaning (SQL)
Filtered out:
- Cancellations (`InvoiceNo` starts with `C`)
- Returns / negative rows (`Quantity <= 0`)
- Invalid prices (`UnitPrice <= 0`)
- Missing customers (`CustomerID IS NULL`)

### 2) RFM Metrics (SQL)
Per customer:
- **Recency (days)** = days since last purchase  
- **Frequency** = count of unique invoices  
- **Monetary** = total revenue sum  

### 3) RFM Scoring (SQL)
Quintile scoring using window functions:
- **Recency**: smaller is better → mapped to higher score (1–5)
- **Frequency / Monetary**: larger is better (1–5)

### 4) Segmentation (SQL)
Rule-based segments:
- **VIP / Champions**
- **Loyal / Regular**
- **New Customers**
- **At-Risk**
- **Lost**
- **Other**

### 5) Export for BI (Python)
Exports Postgres tables into CSV for reporting:
- `outputs/rfm_segments.csv` (customer-level)
- `outputs/rfm_segment_summary.csv` (segment-level)

---

## Key Results
- Customers segmented: **4,338**
- Total revenue (after cleaning): **£8.91M**
- New Customers drive **48.8% of revenue** despite being only 14.9% of the base
- **1,548 At-Risk customers** represent a £847K recovery opportunity
- VIP / Champions (280 customers) show recent purchase behaviour — high retention priority

---

## Business Insights
| Segment | Action |
|---|---|
| New Customers | High avg spend (£6,744) — prioritise onboarding to convert to Loyal |
| At-Risk | 1,548 customers — launch win-back email campaign with discount code |
| VIP / Champions | Protect with loyalty rewards — any churn here is high revenue loss |
| Lost | Small group (7) — low priority for re-engagement |

---

## Dashboard (Power BI)
### Overview
![Overview](powerbi/dashboard_screenshots/01_overview.png)

### Customer Explorer
![Customer Explorer](powerbi/dashboard_screenshots/02_customer_explorer.png)

---

## Outputs
- `outputs/rfm_segments.csv`
- `outputs/rfm_segment_summary.csv`

---

## Project Structure
```text
rfm-segmentation/
├─ src/
│  ├─ export_rfm.py
│  ├─ .env.example
│  └─ .env (local only; not committed)
├─ sql/
│  └─ (your SQL scripts)
├─ outputs/
│  ├─ rfm_segment_summary.csv
│  └─ rfm_segments.csv
└─ powerbi/
   └─ dashboard_screenshots/
      ├─ 01_overview.png
      └─ 02_customer_explorer.png
```
