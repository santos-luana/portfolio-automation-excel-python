# Report Automation with Python and Excel

## Context
Operational and industrial environments often rely on repetitive Excel reports built manually from multiple data sources. This process is time-consuming, error-prone, and limits the analyst’s ability to focus on insights rather than execution.

This project demonstrates how Python can be used to automate the generation and cleaning of Excel-based reports, improving efficiency, consistency, and decision support.

---

## Problem
Manual report generation usually involves:
- Cleaning raw data exported from systems
- Standardizing column names and formats
- Aggregating indicators
- Rebuilding the same Excel report periodically

This workflow increases operational risk and consumes valuable analyst time.

---

## Solution
A Python-based automation pipeline that:
- Reads raw Excel data
- Cleans and standardizes the dataset
- Generates a structured report automatically
- Exports the final result to Excel, ready for analysis or dashboards

The solution was designed with operational KPIs in mind, commonly used in industrial and logistics contexts.

---

## Project Structure
- `data/raw/`  
  Raw input Excel files used by the automation script.

- `scripts/`  
  Python scripts responsible for data cleaning and report generation.

- `output/`  
  Automatically generated Excel reports.

- `README.md`  
  Project documentation and usage instructions.

- `requirements.txt`  
  Python dependencies required to run the project.

- `.gitignore`  
  Files and folders ignored by Git version control.

---

## Technologies Used
- Python
- pandas
- numpy
- Excel (.xlsx)
- Git & GitHub

---

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/santos-luana/portfolio-automation-excel-python.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the automation script:
```bash
python scripts/generate_report.py
```
## Results
- Reduced manual processing time
- Standardized dataset ready for analysis
- Reproducible and scalable reporting process

## Next Improvements
- Add validation checks for missing or inconsistent data
- Parameterize KPIs and time windows
- Integrate with Power BI or databases