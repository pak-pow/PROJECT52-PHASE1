import matplotlib.pyplot as plt
import numpy as np

# Generate 100 days of data
days = np.arange(1, 101)

# start price at 100usd and then add flunctuations everyday
price_changes = np.random.uniform(-2,1,100)
prices = 100 + np.cumsum(price_changes)

# visualize 
# while also setting the window size into 10 inches by 6 inches
plt.figure(figsize=(10, 6)) 

# plot the prices over days
plt.plot(days, prices, color='#00ff88', linestyle='-', linewidth=2, label='Crypto-Sim Value')

# decorating
plt.title('Market Trend Simulation (Week 4)', fontsize=16, fontweight='bold')
plt.xlabel('Days Passed')
plt.ylabel('Asset Price ($)')
plt.grid(True, alpha=0.3, linestyle='--') 
plt.legend() 

# Dark Mode Theme 
plt.style.use('dark_background')
plt.gca().set_facecolor('#ffffff') 
plt.gcf().set_facecolor('#ffffff')

# 4. THE REVEAL
print("Generating Plot...")
plt.show()