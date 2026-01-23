import matplotlib.pyplot as plt # type: ignore
import pandas as pd
import os

# file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dataset", "vgsales.csv")

# loading the data
df = pd.read_csv(file_path)

# droping the rows that have empty or missing info in them
df.dropna(inplace=True)

# top 10 platforms
platform_counts = df['Platform'].value_counts().head(10)

# count the number of games for each genre
genre_counts = df['Genre'].value_counts()

fig, axs = plt.subplots(1, 2, figsize=(15, 7)) # 1 Row, 2 Columns

# plot(kind='bar') is a Pandas shortcut that uses Matplotlib automatically!
platform_counts.plot(kind='bar', ax=axs[0], color='#00ff88', edgecolor='black')
axs[0].set_title('Top 10 Consoles by Game Count', fontsize=14, fontweight='bold', color='black')
axs[0].set_ylabel('Number of Games Released')
axs[0].grid(axis='y', alpha=0.2)

# Pie charts are great for "Part of a Whole"
genre_counts.plot(kind='pie', ax=axs[1], autopct='%1.1f%%', startangle=90, cmap='cool')
axs[1].set_ylabel('') 
axs[1].set_title('Most Popular Game Genres', fontsize=14, fontweight='bold', color='black')

fig.suptitle('VIDEO GAME SALES ANALYSIS (1980-2020)', fontsize=20, color='black')
plt.tight_layout()
print("Dashboard Generated.")
plt.show()