# ETL Pipeline Automation Script
import pandas as pd
import mysql.connector

# === CONFIGURABLE PARAMETERS ===
INPUT_FILE = 'data.csv'
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASS = 'YES'         # <-- Change if needed!
MYSQL_DB   = 'etl_demo'
MYSQL_TABLE = 'sales'

# === EXTRACT ===
df = pd.read_csv(INPUT_FILE)
print("[Extract] Data read from CSV:")
print(df)

# === TRANSFORM ===
df['name'] = df['name'].str.upper()
df = df.drop_duplicates()
print("\n[Transform] Data after cleaning:")
print(df)

# === LOAD ===
try:
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASS,
        database=MYSQL_DB
    )
    cursor = conn.cursor()
    # Insert each row into MySQL
    for _, row in df.iterrows():
        cursor.execute(
            f"REPLACE INTO {MYSQL_TABLE} (id, name, amount) VALUES (%s, %s, %s)",
            tuple(row)
        )
    conn.commit()
    print("\n[Load] Data loaded into MySQL successfully!")
except Exception as e:
    print("\n[Error]", e)
finally:
    if 'cursor' in locals(): cursor.close()
    if 'conn' in locals(): conn.close()
#end
