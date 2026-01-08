import pandas as pd
from pathlib import Path


# Paths
RAW_DATA_PATH = Path("data/raw/production_data.xlsx")
OUTPUT_PATH = Path("output/automated_report.xlsx")

# Create output folder if it does not exist
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_excel(RAW_DATA_PATH)


# Data cleaning
df.columns = df.columns.str.lower().str.replace(" ", "_")

df = df.dropna()

# Feature engineering / KPIs
df["defect_rate"] = df["defects"] / df["production"]

summary = df.groupby("date").agg(
    total_production=("production", "sum"),
    total_defects=("defects", "sum"),
    avg_downtime=("downtime_minutes", "mean"),
    avg_defect_rate=("defect_rate", "mean")
).reset_index()


# Export report
summary.to_excel(OUTPUT_PATH, index=False)

print("Automated report generated successfully.")
