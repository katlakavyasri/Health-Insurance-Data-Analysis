# Health-Insurance-Data-Analysis
# Health Insurance Data Deep Dive

## Project Overview

This project provides an end-to-end data analysis solution for a health insurance dataset. It covers the complete data pipeline from Extract, Transform, Load (ETL) operations using Python, setting up a relational database using SQLite, to developing an interactive business intelligence dashboard in Power BI. The goal is to uncover key insights into insurance costs, policyholder demographics, and regional impacts.

## Key Features & Deliverables

* **Data Cleaning & Transformation:** Python scripts for handling missing values, standardizing data formats, and feature engineering (e.g., BMI categories, age bins, handling negative costs).
* **Relational Database:** A clean SQLite database (`health_insurance_db.sqlite`) containing the processed data, ready for efficient querying.
* **Exploratory Data Analysis (EDA):** Python scripts and generated plots to understand data distributions, relationships, and initial trends.
* **Interactive Power BI Dashboard:** A comprehensive and interactive dashboard (`Health Insurance Data Deep Dive.pbix`) offering various insights through visualizations.
* **Key Performance Indicators (KPIs):** At-a-glance metrics for total policyholders, average insurance cost, and total insurance cost.
* **Organized Project Structure:** A clean repository structure for easy navigation and understanding.

## Technologies Used

* **Python:** For ETL processes and Exploratory Data Analysis.
    * `pandas`: Data manipulation and analysis.
    * `sqlite3`: Interacting with SQLite databases.
    * `matplotlib.pyplot`: Data visualization.
    * `seaborn`: Enhanced data visualization.
* **SQL (SQLite):** For structured data storage and management.
* **Power BI Desktop:** For creating interactive dashboards and business intelligence reports.
* **Git & GitHub:** For version control and collaborative project hosting.

## Project Structure
```
# --- Create Main Project Subdirectories ---

# Create the 'data' directory for raw and processed CSV files
mkdir data

# Create the 'scripts' directory for your Python scripts
mkdir scripts

# Create the 'powerbi' directory for your Power BI report and related files
mkdir powerbi

# Create the 'plots' directory for your generated image files
mkdir plots

# --- File Placement (Manual Steps) ---

echo "--- Now, manually move your files into these newly created directories: ---"

echo ""
echo "Move your original and cleaned CSVs into the 'data' folder:"
echo "    - Insurance_dataset.csv"
echo "    - Insurance_dataset_cleaned_processed.csv"

echo ""
echo "Move your Python scripts into the 'scripts' folder:"
echo "    - process_insurance_data.py"
echo "    - etl_script.py"
echo "    - insurance_eda.py"

echo ""
echo "Move your Power BI files into the 'powerbi' folder:"
echo "    - Health Insurance Data Deep Dive.pbix"
echo "    - (Optional) health_insurance_db.sqbpro"

echo ""
echo "Move your generated plot images into the 'plots' folder:"
echo "    - categorical_distributions.png"
echo "    - insurance_cost_by_gender.png"
echo "    - insurance_cost_by_region.png"
echo "    - insurance_cost_by_smoker.png"
echo "    - (Any other plot images)"
echo "    - (Any Power BI dashboard screenshots, e.g., powerbi_overview.png)"

echo ""
echo "Ensure these main files are directly in your Health-Insurance-Data-Analysis/ root directory:"
echo "    - .gitignore"
echo "    - README.md"
echo "    - health_insurance_db.sqlite"

echo ""
echo "Once you've moved the files, remember to stage, commit, and push these changes to GitHub!"
echo "    git add ."
echo "    git commit -m \"Organize project files into structured directories\""
echo "    git push origin main"

```


To explore or replicate this project, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/katlakavyasri/Health-Insurance-Data-Analysis.git](https://github.com/katlakavyasri/Health-Insurance-Data-Analysis.git)
    cd Health-Insurance-Data-Analysis
    ```
2.  **Set up Python Environment:**
    * It's recommended to create a virtual environment:
        ```bash
        python -m venv venv
        # On Windows:
        .\venv\Scripts\activate
        # On macOS/Linux:
        source venv/bin/activate
        ```
    * Install necessary libraries:
        ```bash
        pip install pandas matplotlib seaborn
        ```
3.  **Run ETL & EDA Scripts:**
    * First, ensure `Insurance_dataset.csv` is in the `data/` folder.
    * Run `process_insurance_data.py` to clean the data and create `Insurance_dataset_cleaned_processed.csv`:
        ```bash
        python scripts/process_insurance_data.py
        ```
    * Run `etl_script.py` to load the processed data into `health_insurance_db.sqlite`:
        ```bash
        python scripts/etl_script.py
        ```
    * Run `insurance_eda.py` to generate exploratory plots:
        ```bash
        python scripts/insurance_eda.py
        ```
4.  **Explore Power BI Dashboard:**
    * Open `powerbi/Health Insurance Data Deep Dive.pbix` using Power BI Desktop.
    * The report will connect to `health_insurance_db.sqlite` (ensure the path in Power BI's data source settings is correct relative to the .pbix file or set to an absolute path if moved).
    * Interact with the dashboard, apply filters, and explore the various pages.

## Power BI Dashboard Overview

The Power BI report is structured across **four key pages** for logical data exploration and detailed analysis:

* **Overview:** Provides key performance indicators (KPIs) and high-level summaries of insurance costs and policyholder demographics, acting as your executive summary.
* **Cost & Distribution Analysis:** Delivers a deeper dive into insurance cost patterns across regions, smoker statuses, and BMI categories, utilizing various comparison and hierarchical charts.
* **Policyholder Demographics:** Focuses on the characteristics of policyholders, including age distribution, BMI categories, number of children, and other relevant demographic breakdowns.
* **Dashboard:** This page can serve as a consolidated view or an alternative summary, perhaps focusing on a specific aspect or a high-level visual aggregation of insights.

Interactive filters (slicers) for `Region`, `Age`, `Gender`, `Smoker Status`, and `BMI Category` allow for dynamic data exploration across all visuals.

---

**Author:** Kavya Sri Katla