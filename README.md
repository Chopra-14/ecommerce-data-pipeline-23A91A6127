# 🛒 E-Commerce Data Pipeline Project

**Student Name:** Konakalla Chopra Lakshmi Sathvika  
**Roll Number:** 23A91A6127  
**Submission Date:** 27-12-2025  

---

![Data Pipeline CI](https://github.com/Chopra-14/ecommerce-data-pipeline-23A91A6127/actions/workflows/ci.yml/badge.svg)

---

## 📌 Project Architecture

This project implements a complete **end-to-end ETL pipeline** for an e-commerce analytics platform.

### 🔄 Data Flow Diagram

Raw CSV Data
↓
Staging Schema
↓
Production Schema
↓
Warehouse (Star Schema)
↓
Analytics Aggregates
↓
BI Dashboards (Power BI / Tableau)

yaml
Copy code

---

## 🧰 Technology Stack

| Layer | Technology |
|------|------------|
| Data Generation | Python (Faker) |
| Database | PostgreSQL |
| ETL | Python (Pandas, SQLAlchemy) |
| Orchestration | Python Scheduler |
| BI Tool | Power BI Desktop / Tableau Public |
| Containerization | Docker |
| Testing | Pytest |

---

## 📂 Project Structure

ecommerce-data-pipeline/
│
├── scripts/
│ ├── data_generation/
│ ├── ingestion/
│ ├── transformation/
│ ├── quality_checks/
│ ├── scheduler.py
│ └── pipeline_orchestrator.py
│
├── data/
│ ├── raw/
│ ├── staging/
│ ├── processed/
│
├── dashboards/
│ ├── powerbi/
│ │ └── ecommerce_analytics.pbix
│ └── screenshots/
│
├── docs/
│ ├── architecture.md
│ └── dashboard_guide.md
│
├── tests/
├── requirements.txt
├── README.md
└── docker-compose.yml

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Chopra-14/ecommerce-data-pipeline-23A91A6127.git
cd ecommerce-data-pipeline
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Start Database (Docker)
bash
Copy code
docker-compose up -d
▶️ Running the Pipeline
🔹 Full Pipeline Execution
bash
Copy code
python scripts/pipeline_orchestrator.py
🔹 Individual Steps
bash
Copy code
python scripts/data_generation/generate_data.py
python scripts/ingestion/ingest_to_staging.py
python scripts/transformation/staging_to_production.py
python scripts/transformation/load_warehouse.py
python scripts/transformation/generate_analytics.py
🧪 Running Tests
bash
Copy code
pytest tests/ -v
📊 Dashboard Access
Power BI File: dashboards/powerbi/ecommerce_analytics.pbix

Screenshots: dashboards/screenshots/

🗄️ Database Schemas
🔹 Staging Schema
staging.customers

staging.products

staging.transactions

staging.transaction_items

🔹 Production Schema
production.customers

production.products

production.transactions

production.transaction_items

🔹 Warehouse Schema
warehouse.dim_customers

warehouse.dim_products

warehouse.dim_date

warehouse.dim_payment_method

warehouse.fact_sales

warehouse.agg_daily_sales

warehouse.agg_product_performance

warehouse.agg_customer_metrics

📈 Key Insights from Analytics
Top Performing Category: Electronics

Revenue Trend: Steady monthly growth with seasonal spikes

Customer Insights: Premium customers contribute major revenue share

Geographic Insight: Top 5 states contribute majority of revenue

Payment Preference: UPI and Credit Card dominate transactions

• High-value (Premium) products contribute a disproportionately higher share of total profit despite lower sales volume, indicating strong margins and pricing power.

⚠️ Challenges & Solutions
Challenge	Solution
Data quality issues	Implemented validation checks
Duplicate records	Applied deduplication logic
Schema mismatch	Normalized production tables
Performance	Added aggregate tables
Visualization clarity	Optimized metrics & layouts

🚀 Future Enhancements
Real-time streaming with Apache Kafka

Cloud deployment (AWS / GCP / Azure)

ML-based demand forecasting

Real-time alerts & monitoring

📞 Contact
Name: Konakalla Chopra Lakshmi Sathvika
Roll Number: 23A91A6127
Email: 23a91a6127@aec.edu.in