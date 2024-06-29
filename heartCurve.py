import matplotlib.pyplot as plt
import numpy as np
from math import e
from matplotlib.animation import FuncAnimation

def formula(x, a):
    abs_x = np.abs(x)
    sqrt_term = np.pi - abs_x**2
    pow_term = np.power(abs_x, 2/3)
    result = pow_term + e/3 * np.sqrt(sqrt_term) * np.sin(a * np.pi * abs_x)
    
    # Ensure output is negative where original x was negative
    result = np.where(x < 0, -result, result)
    
    return result

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 7))  # Increased figure height

ax.set_xlabel('x')
ax.set_ylabel('y')

# Create x data
x = np.linspace(0.1, 1.7, 1000)
X = np.linspace(-2.1, 2.1, 2000)

# Initialize the line
line, = ax.plot([], [], 'b-',lw=2)
ax.set_xlim(-2.1, 2.1)
ax.set_ylim(-1.4, 2.4)
ax.set_xticks([])
ax.set_yticks([])

# Create two separate text objects for the title and a value
title = ax.text(0.5, 1.05, 'Heart Curve Visualization', 
                ha='center', va='bottom', transform=ax.transAxes, fontsize=14)
a_text = ax.text(0.5, 0.98, 'a = 0.0', 
                 ha='center', va='top', transform=ax.transAxes, fontsize=12)

# Animation function
def animate(frame):
    a = frame * 0.2  # Increase 'a' slowly
    y = np.append(formula(x[::-1], a), formula(x, a))
    a_text.set_text(f'a = {a:.1f}')
    line.set_data(X, y)

    # color changing condition
    colors = ["black", "gray", "lightblue", "pink", "lightgreen", "purple", "orange", "yellow", "green", "red"]
    color_index = (frame // 100) % len(colors)
    line.set_color(colors[color_index])
    
    return line, a_text

# Create the animation
anim = FuncAnimation(fig, animate, frames=1000, interval=0.1, blit=True, repeat=False)

plt.tight_layout()
plt.subplots_adjust(top=0.9)  # Adjust top margin
plt.show()