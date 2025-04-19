FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY load_data_2_postgres.py load_data_2_postgres.py 
#COPY ../yellow_tripdata_2024-01.csv /app dùng url cho nhanh

ENTRYPOINT [ "python3", "load_data_2_postgres.py" ]