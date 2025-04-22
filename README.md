# Week 1: Basic Setup – Data Engineering with Docker and PostgreSQL

This project demonstrates how to use **Docker** to build a reproducible environment for loading NYC Taxi CSV data into a **PostgreSQL** database using **Python** and **SQLAlchemy**.

## 📁 Folder Structure

This folder contains the following key files:

- `load_data_2_postgres.py`:  
  Python script to load CSV data into a PostgreSQL database using SQLAlchemy and pandas.

- `Dockerfile`:  
  Dockerfile to create an image that installs Python, required packages, and runs the `load_data_2_postgres.py` script.

- `docker-compose.yaml`:  
  (Optional) File to spin up both the PostgreSQL container and the data loading container together.

- `parquet_to_csv.ipynb`:  
  Jupyter Notebook to convert Parquet data to CSV format (for pre-processing).  to activate use command 'docker-compose up -d'


- `postgres_data/`:  
  Volume for PostgreSQL data persistence.


## 🚀 How to Build and Run the Container

### Step 1: Chạy PostgreSQL 13 Bằng Docker

```bash
Chạy lệnh sau trong thư mục week_1_basic_n_setup: powershell
        'docker-compose up -d'
�� Giải thích lệnh:
o docker-compose up -d: Chạy Docker Compose ở chế độ nền (detached mode).
o Tự động tải về PostgreSQL 13 và pgAdmin nếu chưa có.
o Tạo và khởi động các container pgdatabase (PostgreSQL) và pgadmin.



