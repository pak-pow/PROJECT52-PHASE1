# Week 4: Data Visualization with Python

**Category:** Data Analysis | **Status:** Completed

## About

This project is a deep-dive into Python data science tooling. Using a real-world dataset of video game sales (`dataset/vgsales.csv` — a 1.3MB CSV file with thousands of records), several standalone Python scripts were written to explore, analyze, and visualize the data from different angles.

Each script is focused on a specific type of analysis or chart type, making the project a practical reference for the most common data visualization patterns. `main.py` serves as the entry point that ties the scripts together, while `dashboard.py` renders a multi-panel summary view.

## What It Does

A suite of Python data analysis scripts that load a real video game sales dataset and produce multiple chart types: histograms, scatter plots, trend lines, peak analysis charts, and a summary dashboard.

## Learning Objectives

- Loading and cleaning real-world CSV data with `pandas`
- Creating multiple chart types with `matplotlib` and `seaborn`
- Structuring a data project across multiple focused Python scripts
- Reading and interpreting data insights from visualizations

## Project Structure

```
week4_data_viz/
├── main.py                 # Entry point, runs all analysis scripts
├── dashboard.py            # Multi-panel summary dashboard
├── histogram.py            # Histogram visualizations
├── scatter.py              # Scatter plot analysis
├── sales_trend.py          # Sales trend over time
├── peak_analysis.py        # Peak sales analysis
├── video_game_sales.py     # Platform/genre breakdown
└── dataset/
    └── vgsales.csv         # Real-world video game sales dataset (1.3MB)
```

## Tech Stack

- **Language:** Python 3
- **Libraries:** pandas, matplotlib, seaborn
- **Dataset:** Video Game Sales (Kaggle)
