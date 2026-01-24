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


# chart 1 
axs[0].plot(yearly_sale.index, yearly_sale["Global_Sales"], color = "#00ff88", linewidth = 2, marker="o")
axs[0].set_title('The History of Video Game Sales (Global)', fontsize=16, fontweight='bold', color='white')
axs[0].set_ylabel('Millions of Copies Sold')
axs[0].grid(True, alpha = 0.2)
peak_year = yearly_sale["Global_Sales"].idxmax()
peak_sales = yearly_sale["Global_Sales"].max()
axs[0].annotate(
    f'PEAK: {peak_year}', 
    xy=(peak_year, peak_sales), 
    xytext=(peak_year + 2, peak_sales), # type: ignore 
    arrowprops=dict(facecolor='white', shrink=0.05), 
    fontsize=12
    ) 

# chart 2
axs[1].plot(yearly_sale.index, yearly_sale['NA_Sales'], label='North America', color='#00a8ff', linewidth=2)
axs[1].plot(yearly_sale.index, yearly_sale['EU_Sales'], label='Europe', color='#e056fd', linewidth=2)
axs[1].plot(yearly_sale.index, yearly_sale['JP_Sales'], label='Japan', color='#ff7979', linewidth=2)

axs[1].set_title('Regional Sales Trends (Region vs Region)', fontsize=16, fontweight='bold', color='white')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Millions of Copies Sold')
axs[1].legend() # Shows the labels
axs[1].grid(True, alpha=0.2)

fig.suptitle('VIDEO GAME SALES: TIME SERIES ANALYSIS', fontsize=22, color='white')
plt.tight_layout()
print(f"Peak Year identified: {peak_year}")

plt.show()
