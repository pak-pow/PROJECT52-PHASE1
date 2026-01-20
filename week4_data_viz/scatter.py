import matplotlib.pyplot as plt # type: ignore
import numpy as np

# generate 50 students
np.random.seed(42)  

# x axis: hours studied (random numbers between 1 and 10) 
study_hours = np.random.normal(1, 10, 50)

noise = np.random.normal(0,5,50)
scores = 40