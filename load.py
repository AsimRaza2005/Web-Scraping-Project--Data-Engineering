import pandas as pd
import mysql.connector

# Load cleaned data
df = pd.read_csv("lab_tests_data_cleaned.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",        # 🔁 Change this
    password="datascience",    # 🔁 Change this
    database="my_db"     # 🔁 Change this
)

cursor = conn.cursor()

# Create table (if not exists)
create_table = """
CREATE TABLE IF NOT EXISTS lab_tests (
    lab_id INT,
    lab_name VARCHAR(255),
    test_id INT,
    test_name VARCHAR(255),
    fee FLOAT,
    discount FLOAT,
    discount_percentage FLOAT,
    discounted_fee FLOAT,
    test_type VARCHAR(100),
    savings FLOAT
);
"""
cursor.execute(create_table)

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO lab_tests 
        (lab_id, lab_name, test_id, test_name, fee, discount, discount_percentage, discounted_fee, test_type, savings)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Data successfully loaded into MySQL!")
