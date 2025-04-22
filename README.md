# Week 1: Basic Setup

This folder contains:
- `load_data_2_postgres.py`: Script to load CSV data into a PostgreSQL database using SQLAlchemy.
- `Dockerfile`: Docker container that installs dependencies and runs the script.
- `yellow_tripdata_2024-01.csv`: Taxi trip data used as input (optional via --csv_file argument).

## How to Use

You can run the script directly or build a Docker image and run it with parameters like:

```bash
docker build -t ny-taxi .
docker run ny-taxi --user=root --password=root --host=localhost --port=5432 --db=ny_taxi --table_name=yellow_taxi_trips --csv_file="/app/yellow_tripdata_2024-01.csv"
