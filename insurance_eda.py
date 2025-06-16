import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuration ---
# IMPORTANT: Make sure this path correctly points to your cleaned CSV file.
# This should be the same directory where your Insurance_dataset_cleaned.csv is saved.
cleaned_csv_path = r"C:\Users\kavya\OneDrive\portfolio projects\Project 3\Health Insurance\Insurance_dataset_cleaned.csv"

# Set plot style for better aesthetics
sns.set(style="whitegrid")

# --- Step 1: Load the Cleaned Dataset ---
print("--- Loading Cleaned Insurance Dataset ---")
try:
    df = pd.read_csv(cleaned_csv_path)
    print("Cleaned Insurance dataset loaded successfully.")
    print(f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
except FileNotFoundError:
    print(f"Error: The cleaned file was not found at '{cleaned_csv_path}'.")
    print("Please ensure the path is correct and the file exists.")
    exit()
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
    exit()

# --- Optional: Quick Peek and Overall Summary ---
print("\n--- Dataset Overview (First 5 Rows) ---")
print(df.head())

print("\n--- Dataset Summary (All Columns) ---")
print(df.describe(include='all'))

# --- Step 2: Summarize Numerical Data ---
print("\n--- Numerical Data Summary Statistics ---")
numerical_cols = ['Age', 'BMI', 'Number_of_Children', 'Insurance_Cost']
print(df[numerical_cols].describe())

# --- Step 3: Understand Categorical Data (Unique Values and Counts) ---
print("\n--- Categorical Data Unique Values and Counts ---")
categorical_cols = ['Smoker', 'Gender', 'Region']
for col in categorical_cols:
    print(f"\nUnique values and counts for '{col}':")
    print(df[col].value_counts())

# --- Step 4: Identify Relationships (Correlation Matrix) ---
print("\n--- Correlation Matrix for Numerical Columns ---")
correlation_matrix = df[numerical_cols].corr()
print(correlation_matrix)

# --- Step 5: Investigate Insurance_Cost Anomalies (Negative Values) ---
print("\n--- Rows with Negative Insurance_Cost ---")
negative_cost_rows_initial = df[df['Insurance_Cost'] < 0]
if not negative_cost_rows_initial.empty:
    print(negative_cost_rows_initial)
    print(f"\nTotal negative cost rows: {len(negative_cost_rows_initial)}")
else:
    print("No rows found with negative Insurance_Cost.")

# --- NEW STEP: Handle Negative Insurance_Cost Values (Replacing with 0) ---
print("\n--- Handling Negative Insurance_Cost Values ---")
print(f"Min Insurance_Cost BEFORE handling: {df['Insurance_Cost'].min()}")

# Replace negative Insurance_Cost values with 0
df['Insurance_Cost'] = df['Insurance_Cost'].apply(lambda x: max(0, x))

print(f"Min Insurance_Cost AFTER handling: {df['Insurance_Cost'].min()}")
negative_cost_rows_after_handling = df[df['Insurance_Cost'] < 0]
if negative_cost_rows_after_handling.empty:
    print("All negative Insurance_Cost values have been successfully replaced with 0.")
else:
    print(f"Warning: Some negative Insurance_Cost values still remain after handling:\n{negative_cost_rows_after_handling}")

# --- NEW STEP: Quantify the Impact of Smoker on Insurance_Cost ---
print("\n--- Average Insurance Cost by Smoker Status (After Cost Adjustment) ---")
average_cost_by_smoker = df.groupby('Smoker')['Insurance_Cost'].mean()
print(average_cost_by_smoker)


# --- Step 6: Visualize Distributions ---

# 6.1 Histograms for Numerical Columns (Insurance_Cost will now have 0 as minimum)
print("\n--- Generating Histograms for Numerical Columns ---")
plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(2, 2, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}', fontsize=14)
    plt.xlabel(col, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('numerical_distributions.png', dpi=300)
print("Histograms saved to numerical_distributions.png")
plt.close() # Close the plot to free memory

# 6.2 Bar Charts for Categorical Columns
print("\n--- Generating Bar Charts for Categorical Columns ---")
plt.figure(figsize=(18, 6)) # Adjusted figure size to accommodate 3 plots side-by-side
for i, col in enumerate(categorical_cols):
    plt.subplot(1, 3, i + 1) # 1 row, 3 columns
    sns.countplot(x=col, data=df, palette='viridis', order=df[col].value_counts().index) # Order by count
    plt.title(f'Count of {col}', fontsize=14)
    plt.xlabel(col, fontsize=12)
    plt.ylabel('Count', fontsize=12)
plt.tight_layout()
plt.savefig('categorical_distributions.png', dpi=300)
print("Bar charts saved to categorical_distributions.png")
plt.close() # Close the plot to free memory

# --- Step 7: Explore Relationships with Categorical Variables using Box Plots ---

# 7.1 Insurance_Cost vs. Smoker (will reflect the cleaned costs)
print("\n--- Visualizing Insurance_Cost vs. Smoker ---")
plt.figure(figsize=(8, 6))
sns.boxplot(x='Smoker', y='Insurance_Cost', data=df, palette='pastel')
plt.title('Insurance Cost by Smoker Status', fontsize=16)
plt.xlabel('Smoker', fontsize=14)
plt.ylabel('Insurance Cost', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('insurance_cost_by_smoker.png', dpi=300)
print("Box plot for Insurance Cost by Smoker Status saved to insurance_cost_by_smoker.png")
plt.close()

# 7.2 Insurance_Cost vs. Gender
print("\n--- Visualizing Insurance_Cost vs. Gender ---")
plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='Insurance_Cost', data=df, palette='pastel')
plt.title('Insurance Cost by Gender', fontsize=16)
plt.xlabel('Gender', fontsize=14)
plt.ylabel('Insurance Cost', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('insurance_cost_by_gender.png', dpi=300)
print("Box plot for Insurance Cost by Gender saved to insurance_cost_by_gender.png")
plt.close()

# 7.3 Insurance_Cost vs. Region
print("\n--- Visualizing Insurance_Cost vs. Region ---")
plt.figure(figsize=(10, 6))
sns.boxplot(x='Region', y='Insurance_Cost', data=df, palette='pastel', order=df['Region'].value_counts().index)
plt.title('Insurance Cost by Region', fontsize=16)
plt.xlabel('Region', fontsize=14)
plt.ylabel('Insurance Cost', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('insurance_cost_by_region.png', dpi=300)
print("Box plot for Insurance Cost by Region saved to insurance_cost_by_region.png")
plt.close()

print("\n--- All EDA steps completed. Check the generated PNG files in your script's directory. ---")

import pandas as pd

# IMPORTANT: Ensure your df DataFrame is loaded AND updated from previous steps.
# If you are starting a new session, reload your data and apply the cleaning step first:
# cleaned_csv_path = r"C:\Users\kavya\OneDrive\portfolio projects\Project 3\Health Insurance\Insurance_dataset_cleaned.csv"
# df = pd.read_csv(cleaned_csv_path)
# df['Insurance_Cost'] = df['Insurance_Cost'].apply(lambda x: max(0, x))

# Define the path for the new, processed CSV file
output_csv_path = r"C:\Users\kavya\OneDrive\portfolio projects\Project 3\Health Insurance\Insurance_dataset_cleaned_processed.csv"

print(f"\n--- Saving the cleaned DataFrame to '{output_csv_path}' ---")

# Save the DataFrame to CSV, without the index
df.to_csv(output_csv_path, index=False)

print("Cleaned DataFrame saved successfully!")
print(f"You can find the new file at: {output_csv_path}")