
#!/usr/bin/env python
# coding: utf-8

import os
import argparse

from time import time
import pandas as pd
from sqlalchemy import create_engine

def load_data_to_postgres(params):
    # Connect to PostgreSQL database
    local = params.local
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    csv_name = params.csv_file

    if local == 'True':
        os.system(f"wget {csv_name} -O {csv_name}")


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Load data from Parquet file in chunks

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000, index_col=False)

    # Process each chunk
    for df in df_iter:

        t_start = time()
        # Convert columns to datetime
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        # Load chunk into PostgreSQL database
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False)  # Exclude the "index" column

        t_end = time()

        print('inserted another chunk, took %.3f second' % (t_end - t_start))


    engine.dispose()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--local', required=False, help='Check if running locally', default='False')
    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--csv_file', required=True, help='csv_file of the csv file')

    args = parser.parse_args()

    load_data_to_postgres(args)





# python load_data_2_postgres.py --user=root --password=root --host=localhost --port=5432 --db=ny_taxi --table_name=yellow_taxi_trips --csv_file="E:\\Data-Engineering-Handbook\\week_1_basic_n_setup\\data\\CSV\\yellow_tripdata_2024-01.csv"
# chạy lệnh để thay đổi tùy biến hơn

"""#nháp ✅ Import thư viện
import pandas as pd
from sqlalchemy import create_engine
from time import time

# ✅ Khai báo thông tin kết nối PostgreSQL
user = "root"
password = "root"
host = "localhost"     # hoặc 'pgdatabase' nếu chạy trong Docker
port = 5432
db = "ny_taxi"
table_name = "yellow_taxi_data"

# ✅ Đường dẫn tới file CSV hoặc Parquet
csv_file = r"E:\Data-Engineering-Handbook\week_1_basic_n_setup\data\CSV\yellow_tripdata_2024-01.csv"

# parquet_file = "E:/yellow_tripdata_2024-01.parquet"

# ✅ Tạo engine kết nối
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

# ✅ Đọc file theo từng chunk (tránh out of memory)
df_iter = pd.read_csv(csv_file, iterator=True, chunksize=100000)

for df in df_iter:
    t_start = time()

    # ✅ Chuyển datetime nếu có cột thời gian
    if 'tpep_pickup_datetime' in df.columns:
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    if 'tpep_dropoff_datetime' in df.columns:
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # ✅ Ghi vào PostgreSQL
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

    t_end = time()
    print(f"✔️ Inserted a chunk in {t_end - t_start:.2f} seconds")

engine.dispose()"""
