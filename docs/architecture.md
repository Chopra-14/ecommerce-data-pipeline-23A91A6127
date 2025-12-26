```md
# 🏗️ E-Commerce Data Pipeline Architecture

## Overview
This document describes the architecture of the e-commerce analytics platform designed for scalable data processing and business intelligence.

---

## System Components

### 1. Data Generation Layer
- Generates synthetic data using Python Faker
- Outputs CSV files: customers, products, transactions, transaction_items

### 2. Data Ingestion Layer
- Loads CSV data into PostgreSQL staging schema
- Technology: Python + SQLAlchemy
- Pattern: Batch ingestion

### 3. Data Storage Layer
- **Staging:** Raw data
- **Production:** Cleaned & normalized data
- **Warehouse:** Star schema optimized for analytics

### 4. Data Processing Layer
- Data quality validation
- Transformations & enrichment
- SCD Type 2 handling
- Aggregate table generation

### 5. Data Serving Layer
- Pre-aggregated analytical tables
- Optimized SQL queries

### 6. Visualization Layer
- Power BI / Tableau dashboards
- Interactive reports (16+ visuals)

### 7. Orchestration Layer
- Pipeline orchestrator
- Daily scheduler
- Logging & monitoring

---

## Data Models

### Staging Model
- Raw CSV replica
- Minimal validation

### Production Model
- 3NF normalized schema
- Enforced foreign keys
- Data integrity rules

### Warehouse Model (Star Schema)
- 4 Dimension tables
- 1 Fact table
- 3 Aggregate tables
- Optimized for BI queries

---

## Technologies Used

- Python 3.11
- PostgreSQL 15
- Pandas
- SQLAlchemy
- Docker
- Pytest
- Power BI Desktop

---

## Deployment Architecture

- Dockerized PostgreSQL
- Python services run locally
- Config-driven execution
- Portable & scalable design