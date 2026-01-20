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