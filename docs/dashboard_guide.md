# 📊 Dashboard User Guide

## Accessing the Dashboard

### Power BI
- File: dashboards/powerbi/ecommerce_analytics.pbix
- Requirement: Power BI Desktop (Free)

---

## Dashboard Pages

### 📄 Page 1: Executive Summary
**Purpose:** High-level business overview

**Key Metrics:**
- Total Revenue
- Total Transactions
- Average Order Value
- Profit Margin

**Metric Definitions:**
- Total Revenue = Sum of line_total from fact_sales
- Average Order Value = Total Revenue / Total Transactions
- Profit Margin = (Total Profit / Total Revenue) × 100

**Visuals:**
- Monthly revenue trend
- Top categories
- Payment method distribution
- Geographic sales map

---

### 📄 Page 2: Product Performance
**Purpose:** Product-level analysis

**Insights:**
- Top 10 products generate majority revenue
- Electronics has highest profit margin
- Scatter plot shows price vs profitability

---

### 📄 Page 3: Customer Analytics
**Purpose:** Customer behavior insights

**Insights:**
- High-value customers drive revenue
- Payment preferences analysis
- Customer segmentation

---

### 📄 Page 4: Trends & Geography
**Purpose:** Temporal & location analysis

**Insights:**
- Top states dominate sales
- Seasonal revenue spikes
- Weekend sales outperform weekdays

---

## Filters Available
- Date range
- Product category
- Customer state
- Payment method

---

## How to Use the Dashboard

- Selecting a category filters all charts across pages
- Date slicer updates trends dynamically
- Clicking a bar or map region highlights related visuals
- Scatter plots help identify high-price vs high-profit products

---

## Refreshing Data
1. Run ETL pipeline
2. Open Power BI file
3. Click **Refresh**
4. Save dashboard

---

## Business Recommendations
- Focus on high-margin categories
- Target premium customers
- Optimize inventory for peak seasons
- Premium-priced products show higher profitability despite lower sales volume
