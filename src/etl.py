# ==========================================================
# HR Analytics Platform
# ETL Pipeline (Extract, Transform, Load)
#
# Author: Zeinab Dolatshahi
# Description:
# This script loads the IBM HR Analytics dataset,
# performs basic data quality checks,
# and saves a clean copy for further analysis.
# ==========================================================

import pandas as pd
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA = BASE_DIR / "data" / "raw" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
PROCESSED_DATA = BASE_DIR / "data" / "processed" / "employee_attrition_clean.csv"

# Load dataset
df = pd.read_csv(RAW_DATA)

print("=" * 50)
print("Dataset loaded successfully!")
print("=" * 50)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

# Save a clean copy
df.to_csv(PROCESSED_DATA, index=False)

print(f"\nClean dataset saved to:\n{PROCESSED_DATA}")