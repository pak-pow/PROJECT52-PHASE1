import matplotlib.pyplot as plt #type: ignore
import pandas as pd
import os

# file paths same as day 6 / video_game_sales.py
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dataset", "vgsales.csv")
df = pd.read_csv(file_path)

# data cleaning 
df.dropna(inplace=True)

# convert year from 2008.0 to as 2008 for cleaner graphs [if there is]
df["Year"] = df["Year"].astype(int)

# filtering out
df = df[df["Year"] <= 2016]

# group by year
yearly_sale = df.groupby("Year")[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales']].sum()

# visualization and printing it to the window screen
fig, axs = plt.subplots(2,1, figsize=(10, 8))
plt.show()