import pandas as pd
import sqlite3

# --- 2.1 Extract: Load the CSV file ---
# Use the full path provided for the CSV file
csv_file_path = r"C:\Users\kavya\OneDrive\portfolio projects\Project 3\Health Insurance\Insurance_dataset.csv"

try:
    df = pd.read_csv(csv_file_path)
    print("CSV data loaded successfully from the specified path.")
except FileNotFoundError:
    print(f"Error: The file was not found at '{csv_file_path}'.")
    print("Please ensure the path is correct and the file exists.")
    exit() # Exit the script if the file is not found

# --- 2.2 Transform: Data preparation for SQL ---
# Inspect data types and adjust if necessary
print("\nInitial DataFrame Info:")
df.info()

# Clean column names for SQL (replace spaces with underscores, remove special characters)
# This is crucial for SQL compatibility and easier referencing in Power BI.
df.columns = df.columns.str.replace(' ', '_').str.replace('[^0-9a-zA-Z_]', '', regex=True)

print("\nDataFrame Info after transformations:")
df.info()
print("\nFirst 5 rows of transformed data:")
print(df.head())

# --- Add this section to save the cleaned DataFrame to a new CSV file ---
cleaned_csv_output_path = r"C:\Users\kavya\OneDrive\portfolio projects\Project 3\Health Insurance\Insurance_dataset_cleaned.csv"

try:
    df.to_csv(cleaned_csv_output_path, index=False)
    print(f"\nCleaned data successfully saved to '{cleaned_csv_output_path}'.")
except Exception as e:
    print(f"\nError saving cleaned data to CSV: {e}")

# --- 2.3 Load: Write data to SQLite database ---
database_name = 'health_insurance_characteristics.sqlite' # Name for your SQLite database file
table_name = 'HealthInsuranceCharacteristics2023' # Name for your table in the database

conn = None # Initialize conn to None for the finally block

try:
    # Connect to SQLite database (creates the .sqlite file if it doesn't exist)
    conn = sqlite3.connect(database_name)

    # Use to_sql to write the DataFrame to a SQL table.
    # if_exists='replace' will drop the table if it exists and recreate it.
    # if_exists='append' will add rows to an existing table.
    # index=False prevents writing the DataFrame index as a column in SQL.
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    print(f"\nData successfully loaded into '{database_name}' in table '{table_name}'.")

except Exception as e:
    print(f"\nError loading data to database: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")