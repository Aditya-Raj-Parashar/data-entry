"""
database_updater.py

This script updates a Microsoft SQL Server database by creating the database and table if they do not exist,
and inserting data from a CSV file into the specified table.

Requirements:
see requirments.txt

Usage:
- Update the database connection parameters below.
- Run the script with Python.

"""

import pandas as pd
import pyodbc

# Database configuration
server = 'localhost'  # your server name e.g., 'localhost' or 'server_name\instance_name'
database = 'database_name'  # Name of the database you want to create or enter the data
table_name = 'dbo.table_name'  # Name of the table where data will be inserted
csv_file_path = 'C:/Users/xyz.csv'  # CSV file path or for testing you can use the given csv files in the repository data entry\Bank+Customer+Churn


# Create connection string for Windows Authentication
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

# Connect to the database
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    cursor.execute(f"""
    IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '{database}')
    BEGIN
        CREATE DATABASE {database}
    END
    """)
    conn.commit()
    
    # Use the specified database
    cursor.execute(f"USE {database};")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Create table if it doesn't exist
    create_table_query = f"""
    IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}')
    CREATE TABLE {table_name} (
        {', '.join([f"{col} NVARCHAR(255)" for col in df.columns])}
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Insert data into the table
    for index, row in df.iterrows():
        insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['?' for _ in row])})"
        cursor.execute(insert_query, tuple(row))

    conn.commit()
    print(f"Data inserted successfully into {table_name}.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()