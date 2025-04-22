# Sử dụng image chính thức của Python phiên bản 3.9.1 làm base image
FROM python:3.9.1

# Cài đặt công cụ wget để tải file từ internet trong container nếu cần
RUN apt-get install wget -y

# Cài đặt các thư viện Python cần thiết:
# - pandas: để xử lý dữ liệu
# - sqlalchemy: để tạo kết nối với PostgreSQL
# - psycopg2: driver PostgreSQL cho Python
RUN pip install pandas sqlalchemy psycopg2

# Thiết lập thư mục làm việc trong container là /app
WORKDIR /app

# Sao chép file script Python từ máy host vào thư mục làm việc trong container
COPY load_data_2_postgres.py load_data_2_postgres.py

# (Tùy chọn) Không cần copy file CSV nếu bạn sử dụng URL (qua biến --csv_file)
# COPY ../yellow_tripdata_2024-01.csv /app

# Thiết lập entrypoint cho container khi chạy
# Mặc định sẽ chạy file Python load_data_2_postgres.py
ENTRYPOINT [ "python3", "load_data_2_postgres.py" ]
