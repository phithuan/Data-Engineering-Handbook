# Week 1: Basic Setup – Data Engineering with Docker and PostgreSQL

This project demonstrates how to use **Docker** to build a reproducible environment for ingesting NYC Taxi data into a **PostgreSQL** database using **Python**, **pandas**, and **SQLAlchemy**.  
The process includes building a Docker image, running containers via Docker Compose, and loading CSV data into the database.

👉 **Reference:**  
[📘 Week 1 – Docker & SQL Setup Guide](https://de-book.longdatadevlog.com/datacamping/week_1_basics_and_infrastructure/2_docker_sql/index.html)

---

## 📁 Folder Structure

| File / Folder             | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `load_data_2_postgres.py` | Python script to load CSV data into PostgreSQL using SQLAlchemy and pandas. |
| `Dockerfile`              | Builds the image with Python and required libraries to run the script.      |
| `docker-compose.yaml`     | (Optional) Launches PostgreSQL and pgAdmin using Docker Compose.             |
| `parquet_to_csv.ipynb`    | Jupyter Notebook to convert Parquet files to CSV (preprocessing step).      |
| `postgres_data/`          | Volume for PostgreSQL data persistence.                                     |

---

## 🚀 Getting Started

### ✅ Step 1: Launch PostgreSQL and pgAdmin with Docker Compose

Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running.

In **PowerShell** or **Terminal**, navigate to your working directory and run:

```bash
docker-compose up -d
```

💡 **Check running containers:**

```bash
docker ps
```

---

### ✅ Step 2: Build the Docker Image for Ingesting Data

In the same folder (where the Dockerfile is located), build the image:

```bash
docker build -t ny_taxi_ingest:v001 .
```

---

### ✅ Step 3: Run the Data Ingestion Script in a Container

#### ▶️ Using a local CSV file

```powershell
docker run -it `
  -v "E:\Data-Engineering-Handbook\week_1_basic_n_setup\data\CSV\yellow_tripdata_2025-01.csv:/app/yellow_tripdata_2025-01.csv" `
  ny_taxi_ingest:v001 `
  --local=False `
  --user=root `
  --password=root `
  --host=host.docker.internal `
  --port=5432 `
  --db=ny_taxi `
  --table_name=yellow_taxi_trips_2025_01 `
  --csv_file=yellow_tripdata_2025-01.csv
```
