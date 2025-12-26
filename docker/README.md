# Docker Deployment Guide – E-Commerce Data Pipeline

This document explains how to deploy, run, and manage the E-Commerce Data Pipeline using Docker and Docker Compose.

---

## 1. Prerequisites

Ensure the following are installed on your system:

- Docker Engine: version 20.10 or higher
- Docker Compose: version 2.0 or higher

Minimum system requirements:
- RAM: 4 GB minimum (8 GB recommended)
- Disk Space: At least 5 GB free
- OS: Windows / Linux / macOS

Verify installation:

```bash
docker --version
docker compose version
2. Quick Start Guide
Step 1: Build and Start Services
bash
Copy code
docker compose up -d
This starts:

PostgreSQL database container

Pipeline container

Step 2: Verify Services Are Running
bash
Copy code
docker compose ps
Expected:

postgres → healthy

pipeline → running

Step 3: Run the Pipeline Inside Docker
bash
Copy code
docker compose exec pipeline python scripts/pipeline_orchestrator.py
This executes the full ETL pipeline:

Data generation

Ingestion

Transformation

Warehouse loading

Analytics generation

Step 4: Access the Database
bash
Copy code
docker compose exec postgres psql -U admin -d ecommerce_db
Schemas available:

staging

production

warehouse

Step 5: View Logs
bash
Copy code
docker compose logs
For individual services:

bash
Copy code
docker compose logs postgres
docker compose logs pipeline
Step 6: Stop Services
bash
Copy code
docker compose down
Step 7: Clean Up (Remove Volumes & Data)
bash
Copy code
docker compose down -v
docker system prune -f
⚠️ This deletes all database data.

3. Troubleshooting
Port Already in Use
Issue: Port 5432 is already in use
Solution:

bash
Copy code
netstat -ano | findstr 5432
Stop the conflicting service or change the port in docker-compose.yml.

Database Not Ready
Issue: Pipeline starts before database
Solution:
PostgreSQL health checks and depends_on with service_healthy are configured.

Volume Permission Issues
Issue: Permission denied on database volume
Solution:

bash
Copy code
docker compose down -v
docker compose up -d
Container Fails to Start
Issue: Pipeline container exits immediately
Solution:

bash
Copy code
docker compose logs pipeline
Check environment variables and database connectivity.

Network Connectivity Issues
Issue: Pipeline cannot connect to PostgreSQL
Solution:
Ensure the pipeline connects using service name postgres, not localhost.

4. Configuration Details
Environment Variables
Defined in docker-compose.yml:

POSTGRES_DB

POSTGRES_USER

POSTGRES_PASSWORD

DB_HOST=postgres

DB_PORT=5432

Volume Mounts
postgres_data → persists PostgreSQL data

Pipeline logs and outputs persist across restarts

Network Configuration
Default Docker Compose bridge network

Services communicate via service names

Resource Limits
Recommended:

PostgreSQL: 1–2 GB RAM

Pipeline: 1 GB RAM

5. Data Persistence Verification
PostgreSQL data persists across container restarts

Pipeline outputs remain available unless volumes are removed

Verified by stopping and restarting containers without data loss

Summary
This Docker setup ensures:

Proper service isolation

Reliable database initialization

Persistent data storage

Reproducible deployment environment

