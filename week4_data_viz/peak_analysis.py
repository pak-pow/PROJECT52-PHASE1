import matplotlib.pyplot as plt # type: ignore
import pandas as pd
import os

# load file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dataset", "vgsales.csv")
df = pd.read_csv(file_path)

# data cleaning
df.dropna(inplace=True)
df['Year'] = df['Year'].astype(int)

# data filtering, and showing the peak year
df_2008 = df[df['Year'] == 2008]

# what was the top 5 video game sale? during this year?
# sorting the globasl sales (high to low) and take the top 5
top_games = df_2008.sort_values(by="Global_Sales", ascending=False).head(5)

# who was the top 5 publiser during this year?
# grouping the publisher, sum of sales, and sort from high to low
top_publisher = df_2008.groupby("Publisher")["Global_Sales"].sum().sort_values(ascending=False).head(5)

# visualizing 
fig, axs = plt.subplots(1,2, figsize = (16,8))

axs[0].barh(
    top_games["Name"], 
    top_games["Global_Sales"], 
    color = "#00ff88",
    edgecolor = "black"
    )

axs[0].invert_yaxis()
axs[0].set_title('Top 5 Best Selling Games (2008)', fontsize=12, fontweight='bold', color='black')
axs[0].set_xlabel('Global Sales (Millions)')
axs[0].grid(axis='x', alpha=0.2)

axs[1].pie(top_publisher, labels=top_publisher.index, autopct='%1.1f%%', startangle=140, 
           colors=['#e056fd', '#00a8ff', '#ff7979', '#f0932b', '#badc58'],
           explode=(0.1, 0, 0, 0, 0)) # "Pull out" the biggest slice
axs[1].set_title('Market Share by Publisher (2008)', fontsize=14, fontweight='bold', color='black')

fig.suptitle('FORENSIC ANALYSIS: THE YEAR 2008', fontsize=20, color='black')
print(f"Top Game of 2008: {top_games.iloc[0]['Name']}")
plt.tight_layout()
plt.show()