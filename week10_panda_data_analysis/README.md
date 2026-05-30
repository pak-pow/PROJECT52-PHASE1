# Week 10: Pandas Data Analysis

**Category:** Data Analysis | **Status:** Completed

## About

This project revisits data analysis from Week 4, but with a more focused lens: structured analysis of a real-world mobile app dataset. Rather than building multiple chart scripts, this project uses `pandas` to perform the full data analysis pipeline — loading, cleaning, grouping, aggregating, and summarizing — and outputs a clean CSV report.

The dataset (`app_data.csv`) contains mobile app metrics. The analysis in `main.py` processes it, applies grouping and statistical operations, and writes a `Platform_Summary_Report.csv` — a condensed, human-readable summary of the findings.

## What It Does

A Python data analysis script that loads a mobile app metrics dataset, performs cleaning and aggregation with pandas, and exports a summary report as a CSV file.

## Learning Objectives

- Data cleaning: handling missing values, type conversion, and outliers
- Pandas operations: `groupby()`, `agg()`, `describe()`, `value_counts()`
- Exporting processed data to CSV for reporting
- Understanding the full data pipeline from raw input to clean output

## Project Structure

```
week10_panda_data_analysis/
├── main.py                         # Full analysis pipeline
├── app_data.csv                    # Raw input dataset
└── Platform_Summary_Report.csv     # Generated output report
```

## Tech Stack

- **Language:** Python 3
- **Libraries:** pandas
