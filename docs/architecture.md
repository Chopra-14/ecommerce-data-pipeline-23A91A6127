# 🏗️ System Architecture — E-Commerce Data Pipeline

## 📌 Overview
This project implements a **modular, end-to-end ETL data pipeline** for an E-Commerce analytics platform.  
The architecture is designed to be **scalable, idempotent, fault-tolerant, and analytics-ready**, supporting batch processing, monitoring, and BI reporting.

---

## 🔹 High-Level Architecture

┌────────────────────┐
│ Data Generation │
│ (Synthetic CSVs) │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Staging Layer │
│ (Raw Ingestion) │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Data Quality Layer │
│ (Validation & DQ) │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Production Layer │
│ (Cleaned Tables) │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Warehouse Layer │
│ (Star Schema) │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Analytics Layer │
│ (Aggregations) │
└─────────┬──────────┘
↓
┌────────────────────┐
│ BI / Dashboards │
│ (Power BI) │
└────────────────────┘

yaml
Copy code

---

## 🧱 Architecture Layers Explained

### 1️⃣ Data Generation Layer
**Purpose:** Create reproducible synthetic e-commerce data.

- Implemented using Python + Faker
- Generates:
  - Customers
  - Products
  - Transactions
  - Transaction Items
- Output format: CSV
- Idempotent (files overwritten on each run)

📁 Location:
scripts/data_generation/
data/raw/

yaml
Copy code

---

### 2️⃣ Staging Layer
**Purpose:** Raw ingestion without business logic.

- Loads CSVs into PostgreSQL `staging` schema
- Uses `TRUNCATE + INSERT` for idempotency
- Adds metadata columns like `loaded_at`

📁 Location:
scripts/ingestion/
PostgreSQL schema: staging

yaml
Copy code

---

### 3️⃣ Data Quality Layer
**Purpose:** Validate correctness and reliability of data.

Checks performed:
- Referential integrity (orphan records)
- NULL checks on mandatory columns
- Basic consistency rules
- Quality score calculation

Outputs:
- `data_quality_report.json`

📁 Location:
scripts/quality_checks/
data/processed/data_quality_report.json

yaml
Copy code

---

### 4️⃣ Production Layer
**Purpose:** Cleaned and business-ready transactional data.

Key transformations:
- Data cleansing (trim, lowercase emails)
- Business logic application
- Constraint enforcement
- Deduplication

Idempotent behavior:
- Dimensions truncated and reloaded
- Facts inserted safely

📁 Location:
scripts/transformation/staging_to_production.py
PostgreSQL schema: production

markdown
Copy code

---

### 5️⃣ Warehouse Layer (Dimensional Model)
**Purpose:** Analytics-optimized star schema.

Schema design:
- **Fact Table**
  - `fact_sales`
- **Dimension Tables**
  - `dim_customers`
  - `dim_products`
  - `dim_date`
  - `dim_payment_method`
- **Aggregate Tables**
  - `agg_daily_sales`
  - `agg_customer_metrics`
  - `agg_product_performance`

Features:
- Surrogate keys
- SCD handling
- Optimized for BI tools

📁 Location:
scripts/transformation/load_warehouse.py
PostgreSQL schema: warehouse

yaml
Copy code

---

### 6️⃣ Analytics Layer
**Purpose:** Pre-computed analytics for dashboards.

- Executes SQL aggregations
- Exports CSV outputs
- Used by Power BI dashboards

📁 Location:
scripts/transformation/generate_analytics.py
data/processed/analytics/

yaml
Copy code

---

### 7️⃣ Orchestration Layer
**Purpose:** Control execution order and fault handling.

- Executes pipeline steps sequentially
- Stops execution on failure
- Retry logic with exponential backoff
- Generates execution report

📁 Location:
scripts/pipeline_orchestrator.py
data/processed/pipeline_execution_report.json

yaml
Copy code

---

### 8️⃣ Scheduling & Automation
**Purpose:** Fully automated daily pipeline execution.

- Uses Python scheduler
- Prevents concurrent runs
- Executes cleanup after success

📁 Location:
scripts/scheduler.py
scripts/cleanup_old_data.py
logs/scheduler_activity.log

yaml
Copy code

---

### 9️⃣ Monitoring & Alerting
**Purpose:** Continuous pipeline health monitoring.

Monitored dimensions:
- Pipeline execution health
- Data freshness
- Volume anomalies
- Data quality trends
- Database connectivity

Output:
- `monitoring_report.json`

📁 Location:
scripts/monitoring/
data/processed/monitoring_report.json

yaml
Copy code

---

### 🔟 Business Intelligence Layer
**Purpose:** Data visualization and insights.

- Tool: **Power BI**
- Dashboards:
  - Executive Overview
  - Product Performance
  - Customer Analytics
  - Trends & Geography
- Connected directly to PostgreSQL warehouse

📁 Location:
dashboards/powerbi/

yaml
Copy code

---

## 🔐 Key Architecture Principles

| Principle | Implementation |
|--------|----------------|
| Modularity | Separate scripts per pipeline stage |
| Idempotency | TRUNCATE + reload strategy |
| Fault Tolerance | Step-level error handling |
| Observability | Logs, reports, monitoring |
| Scalability | Layered schema design |
| BI-Readiness | Star schema warehouse |

---

## 🧠 Technology Stack

- **Language:** Python
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Scheduling:** Python Scheduler
- **BI Tool:** Power BI
- **Testing:** Pytest + Coverage
- **Version Control:** Git & GitHub

---

## ✅ Conclusion
This architecture ensures a **robust, production-style data pipeline** that supports reliable analytics, automated execution, monitoring, and enterprise-ready BI reporting.

---
