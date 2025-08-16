<<<<<<< HEAD
# ETL Pipeline Automation Project

## Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python, Pandas, and MySQL.

- **Extract:** Reads data from a CSV file.
- **Transform:** Cleans the data by uppercasing names and removing duplicates.
- **Load:** Inserts the transformed data into a MySQL database table.

## Files
- `etl_script.py` : Main Python script for ETL operations.
- `data.csv` : Input data with simple sales records.

## Requirements
- Python 3.x
- pandas
- mysql-connector-python
- MySQL Server

## MySQL Table Creation
Run the following in MySQL Workbench or CLI before the script:

CREATE DATABASE etl_demo;
USE etl_demo;
CREATE TABLE sales (
id INT PRIMARY KEY,
name VARCHAR(255),
amount INT
);


## How to Run

1. Install Python dependencies:
    ```
    pip install pandas mysql-connector-python
    ```
2. Update the MySQL username/password in `etl_script.py` if needed.
3. Run the script:
    ```
    python etl_script.py
    ```

Data will be loaded into your MySQL table and a message will confirm success.

---

## Example Output

[Extract] Data read from CSV:
id name amount
0 1 John 100
1 2 Jane 150
2 3 Bob 200

[Transform] Data after cleaning:
id name amount
0 1 JOHN 100
1 2 JANE 150
2 3 BOB 200

[Load] Data loaded into MySQL successfully!


---

## Customization
- You can use a larger or more complex CSV as you wish.
- Add more data validation, logging, or config arguments for enhancement.

---

## Author
Sriram Karthikeya Kota


---
=======
# ETL_PROJECT
>>>>>>> c296681f94eff5c70d8d3db4b643e12f93a57211
