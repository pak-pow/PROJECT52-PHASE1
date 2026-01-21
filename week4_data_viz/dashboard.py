import matplotlib.pyplot as plt # type: ignore
import numpy as np 

np.random.seed(42)

# data a: stock trends (line)
days = np.arange(1,51)
stock_price = 100 + np.cumsum(np.random.uniform(-5,5,50))

# data b: exam scores (histogram)
scores = np.random.normal(75,10,200)

# Data C: Study vs Grades (Scatter)
study_hours = np.random.uniform(1, 10, 50)
grades = 40 + (study_hours * 5) + np.random.normal(0, 5, 50)

# Data D: Language Popularity (Bar Chart - NEW!)
languages = ['Python', 'JS', 'C++', 'Rust', 'Go']
popularity = [90, 85, 70, 60, 50]

# Create a 2x2 grid (2 rows, 2 columns)
# figsize=(12, 10) makes the window large enough to see everything
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Apply Dark Mode manually to the Figure background
fig.patch.set_facecolor('#ffffff') # type: ignore
plt.style.use('dark_background')

# TOP LEFT [0, 0]: Stock Trend
axs[0, 0].plot(days, stock_price, color='#00ff88', linewidth=2)
axs[0, 0].set_title('Market Trend (Line)', fontsize=12, color='white')
axs[0, 0].grid(True, alpha=0.2)
axs[0, 0].set_facecolor('#333')

# TOP RIGHT [0, 1]: Exam Distribution
axs[0, 1].hist(scores, bins=20, color='#ff00ff', alpha=0.7)
axs[0, 1].set_title('Test Scores (Histogram)', fontsize=12, color='white')
axs[0, 1].grid(axis='y', alpha=0.2)
axs[0, 1].set_facecolor('#333')

# BOTTOM LEFT [1, 0]: Correlation
axs[1, 0].scatter(study_hours, grades, color='cyan', alpha=0.8)
axs[1, 0].set_title('Study vs Grades (Scatter)', fontsize=12, color='white')
axs[1, 0].grid(True, alpha=0.2)
axs[1, 0].set_facecolor('#333')

# BOTTOM RIGHT [1, 1]: Tech Stack (Bar Chart)

axs[1, 1].bar(languages, popularity, color=['#306998', '#F7DF1E', '#00599C', '#dea584', '#00ADD8'])
axs[1, 1].set_title('Dev Language Popularity (Bar)', fontsize=12, color='white')
axs[1, 1].set_facecolor('#333')

# Super Title for the whole window
fig.suptitle('DASHBOARD', fontsize=18, fontweight='bold', color='#111')

# Tight Layout prevents the graphs from overlapping each other
plt.tight_layout()

# Show the Masterpiece
plt.show()