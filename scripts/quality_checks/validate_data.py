import json
from datetime import datetime
from pathlib import Path

import yaml
from sqlalchemy import create_engine, text


# --------------------------------------------------
# Load configuration
# --------------------------------------------------
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

DB_URL = config["database"]["url"]

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = OUTPUT_DIR / "data_quality_report.json"


# --------------------------------------------------
# Quality Checks
# --------------------------------------------------
def run_quality_checks():
    engine = create_engine(DB_URL)

    orphan_count = 0
    null_count = 0

    with engine.connect() as conn:

        # ------------------------------------------
        # Referential Integrity Checks
        # ------------------------------------------
        orphan_customer_txn = conn.execute(text("""
            SELECT COUNT(*)
            FROM staging.transactions t
            LEFT JOIN staging.customers c
            ON t.customer_id = c.customer_id
            WHERE c.customer_id IS NULL
        """)).scalar()

        orphan_item_txn = conn.execute(text("""
            SELECT COUNT(*)
            FROM staging.transaction_items i
            LEFT JOIN staging.transactions t
            ON i.transaction_id = t.transaction_id
            WHERE t.transaction_id IS NULL
        """)).scalar()

        orphan_item_product = conn.execute(text("""
            SELECT COUNT(*)
            FROM staging.transaction_items i
            LEFT JOIN staging.products p
            ON i.product_id = p.product_id
            WHERE p.product_id IS NULL
        """)).scalar()

        orphan_count = (
            orphan_customer_txn
            + orphan_item_txn
            + orphan_item_product
        )

        # ------------------------------------------
        # NULL Checks (Mandatory Fields)
        # ------------------------------------------
        null_customers = conn.execute(text("""
            SELECT COUNT(*)
            FROM staging.customers
            WHERE customer_id IS NULL
        """)).scalar()

        null_products = conn.execute(text("""
            SELECT COUNT(*)
            FROM staging.products
            WHERE product_id IS NULL OR price IS NULL
        """)).scalar()

        null_transactions = conn.execute(text("""
            SELECT COUNT(*)
            FROM staging.transactions
            WHERE transaction_id IS NULL OR customer_id IS NULL
        """)).scalar()

        null_items = conn.execute(text("""
            SELECT COUNT(*)
            FROM staging.transaction_items
            WHERE item_id IS NULL OR transaction_id IS NULL OR product_id IS NULL
        """)).scalar()

        null_count = (
            null_customers
            + null_products
            + null_transactions
            + null_items
        )

    # --------------------------------------------------
    # Quality Score Calculation
    # --------------------------------------------------
    quality_score = max(0, 100 - (orphan_count + null_count) * 10)

    # --------------------------------------------------
    # Report Structure (MATCHES TESTS EXACTLY)
    # --------------------------------------------------
    report = {
        "data_quality_summary": {
            "quality_score": quality_score,
            "critical_issues": orphan_count + null_count
        },
        "generated_at": datetime.utcnow().isoformat()
    }

    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=4)

    print("✅ Data quality report generated successfully")


# --------------------------------------------------
# Main
# --------------------------------------------------
if __name__ == "__main__":
    run_quality_checks()
