import matplotlib.pyplot as plt # type: ignore
import numpy as np

# Generate 100 days of data
days = np.arange(1, 101)

# Asset A (Volatile Crypto)
# High fluctuation (-3 to +3)
changes_a = np.random.uniform(-3, 3, 100)
price_a = 100 + np.cumsum(changes_a)

# Asset B (Stable Gold)
# Low fluctuation (-1 to +1)
changes_b = np.random.uniform(-1, 1, 100)
price_b = 100 + np.cumsum(changes_b)

# visualize 
# while also setting the window size into 10 inches by 7 inches
plt.figure(figsize=(12, 7)) 

# Plot both lines
plt.plot(days, price_a, color='#00ff88', linewidth=2, label='Crypto (Volatile)')
plt.plot(days, price_b, color='#ffcc00', linewidth=2, linestyle='--', label='Gold (Stable)')

# Fill the area between the two lines
# "where" argument checks the logic.
# If A > B, fill Green. If B > A, fill Red.
plt.fill_between(days, price_a, price_b, where=(price_a > price_b),  # type: ignore
                 interpolate=True, color='#00ff88', alpha=0.1)

plt.fill_between(days, price_a, price_b, where=(price_a <= price_b),  # type: ignore
                 interpolate=True, color='#ff0055', alpha=0.1)

# 4. ANNOTATIONS (Pointing to specific events)
# Let's point to the highest price of Crypto
max_price = np.max(price_a)
max_day = days[np.argmax(price_a)]

plt.annotate(f'All Time High (${max_price:.2f})', 
             xy=(max_day, max_price),            # Arrow points to this (x,y)
             xytext=(max_day+5, max_price+5),    # Text sits here
             arrowprops=dict(facecolor='white', shrink=0.05))

# decorating
plt.title('Asset Performance Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Days Trading')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True, alpha=0.2)

# Dark Mode Theme 
plt.style.use('dark_background')
plt.gca().set_facecolor('#ffffff') 
plt.gcf().set_facecolor('#ffffff')

# 4. THE REVEAL
print("Generating Plot...")
plt.show()