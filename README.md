# RFM Customer Segmentation (PostgreSQL + Python + Power BI)

## Overview

This project segments customers using the RFM framework:

- **Recency** (days since last purchase)
- **Frequency** (number of invoices)
- **Monetary** (total revenue)

The pipeline is:

1. Load and clean transactions in **PostgreSQL**
2. Build RFM metrics + scores with **SQL window functions**
3. Export results to CSV with **Python**
4. Visualize segments in **Power BI**

## Dataset

Online Retail transactions (2010–2011).

## Outputs

- `outputs/rfm_segment_summary.csv` — segment-level KPIs
- `outputs/rfm_segments.csv` — customer-level RFM + segment labels (4338 customers)

## Power BI

Screenshots:

- `powerbi/dashboard_screenshots/01_overview.png`
- `powerbi/dashboard_screenshots/02_customer_explorer.png`

## How to run

### 1) Run SQL in Postgres

Execute:

- `sql/rfm.sql`

### 2) Export CSVs

Create `src/.env` locally (do not commit it):
