import matplotlib.pyplot as plt # type: ignore
import numpy as np

# generate 50 students
np.random.seed(42)  

# x axis: hours studied (random numbers between 1 and 10) 
study_hours = np.random.normal(1, 10, 50)

# Y Axis: Test Scores
# Formula: Base Score (40) + (Hours * 5) + Random Noise (-10 to +10)
# This simulates that studying helps (slope of 5), but some people are just lucky/unlucky (noise)
noise = np.random.normal(0,5,50)
scores = 40 + (study_hours * 5) + noise

# clip scores to be realistic ranging from 0-100
scores = np.clip(scores, 0, 100)

# np.polyfit calculates the slope (m) and y-intercept (b) of the best fit line
# "1" means we want a 1st-degree polynomial (a straight line)
m, b = np.polyfit(study_hours, scores, 1)

# creating line equation: y = mx + b
trend_line = (m * study_hours) + b

# visualization
plt.figure(figsize=(10,6))

# The Dots (Actual Student Data)
# s=100 sets the size of the dots
# c=scores colors the dots based on how high the score is (Cool effect)
plt.scatter(study_hours, scores, c=scores, cmap='cool', alpha=0.8, s=100, edgecolors='white', label='Student Data')

# The Line (The Mathematical Trend)
plt.plot(study_hours, trend_line, color='white', linewidth=3, linestyle='--', label=f'Trend Line (Slope: {m:.2f})')

# 4. DECORATION
plt.title('Effect of Study Hours on Exam Score', fontsize=16, fontweight='bold')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True, alpha=0.3)
plt.colorbar(label='Score Intensity') # Adds the color scale bar on the right

# Theme
plt.style.use('dark_background')
plt.gca().set_facecolor('#1a1a1a') 

# 5. THE REVEAL
print(f"Calculated Trend: For every 1 hour studied, score increases by {m:.2f} points.")
plt.show()

