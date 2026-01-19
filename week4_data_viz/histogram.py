import matplotlib.pyplot as plt # type: ignore
import numpy as np

# generating 1000 students exam scores
# mean (average) = 75, standard deviation = 10
np.random.seed(42) # ensuring we get the same "random" numbers each time we run this
scores = np.random.normal(75,10,1000)

# clipping scores so that no one gets less than 0 or more than 100
scores = np.clip(scores,0,100)

# visualize histogram
plt.figure(figsize=(10,6))

# plt.hist returns 3 values, but we only need the plot
# bins=30 means "split the scores into 30 buckets"
# alpha=0.7 makes the bars slightly see-through
# color='#ff00ff' is Magenta (Cyberpunk style)
plt.hist(scores, bins=30, color='#ff00ff', edgecolor='black', alpha=0.7)

plt.axvline(60, color='red', linestyle='dashed', linewidth=2, label='Passing Grade (60)')

plt.axvline(scores.mean(), color='yellow', linestyle='dashed', linewidth=2, label=f'Average ({scores.mean():.1f})')

plt.title('Distribution of 1000 Exam Scores', fontsize=16)
plt.xlabel('Score (0-100)')
plt.ylabel('Number of Students')
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.style.use('dark_background')
plt.gca().set_facecolor('#ffffff') 

print("Analyzing Test Results...")
plt.show()