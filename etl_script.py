import pandas as pd
import sqlite3

# IMPORTANT: Make sure this path points to your NEWLY SAVED processed CSV file.
# This should be the same directory where your Insurance_dataset_cleaned_processed.csv is saved.
processed_csv_path = r"C:\Users\kavya\OneDrive\portfolio projects\Project 3\Health Insurance\Insurance_dataset_cleaned_processed.csv"

# --- 2.1 Extract: Load the CSV file ---
print("\n--- Starting ETL Process ---")
try:
    # Load the processed CSV with adjusted Insurance_Cost
    df_etl = pd.read_csv(processed_csv_path)
    print("Processed CSV data loaded successfully for ETL.")
except FileNotFoundError:
    print(f"Error: '{processed_csv_path}' not found.")
    print("Please ensure the file is in the specified directory.")
    exit()
except Exception as e:
    print(f"An error occurred during CSV loading for ETL: {e}")
    exit()

# --- 2.2 Transform: Data preparation for SQL ---
# Inspect initial data types for the ETL DataFrame
print("\nInitial DataFrame Info for ETL:")
df_etl.info()

# Clean column names for SQL (replace spaces and special characters with underscores)
original_columns = df_etl.columns.tolist()
df_etl.columns = df_etl.columns.str.replace(' ', '_').str.replace('[^0-9a-zA-Z_]', '', regex=True)
print("\nColumn names cleaned for SQL compatibility:")
print(f"Original columns: {original_columns}")
print(f"Cleaned columns: {df_etl.columns.tolist()}")

# Ensure any boolean columns are converted to integer (0 or 1) if present
# (Based on our data, 'Smoker' is already 'yes'/'no' strings, not booleans)
# For example, if you had a 'HasDiabetes' boolean column:
# if 'HasDiabetes' in df_etl.columns and df_etl['HasDiabetes'].dtype == 'bool':
#     df_etl['HasDiabetes'] = df_etl['HasDiabetes'].astype(int)

print("\nDataFrame Info after column name transformations:")
df_etl.info()
print("\nFirst 5 rows of transformed data for ETL:")
print(df_etl.head())

# --- 2.3 Load: Write data to SQLite database ---
database_name = 'health_insurance_db.sqlite' # Name for your SQLite database file
table_name = 'HealthInsuranceData' # Name for your table in the database
full_db_path = r"C:\Users\kavya\OneDrive\portfolio projects\Project 3\Health Insurance" + "\\" + database_name

print(f"\nAttempting to load data into SQLite database: '{full_db_path}'")

conn = None # Initialize conn to None
try:
    # Connect to SQLite database (creates the .sqlite file if it doesn't exist)
    conn = sqlite3.connect(full_db_path)

    # Use to_sql to write the DataFrame to a SQL table.
    # if_exists='replace' will drop the table if it exists and recreate it.
    # if_exists='append' will add rows to an existing table.
    # index=False prevents writing the DataFrame index as a column in SQL.
    df_etl.to_sql(table_name, conn, if_exists='replace', index=False)

    print(f"\nData successfully loaded into '{database_name}' in table '{table_name}'.")

except Exception as e:
    print(f"\nError loading data to database: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")

print("\n--- ETL Process Completed. ---")