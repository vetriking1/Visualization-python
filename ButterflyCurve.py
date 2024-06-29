import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define the x values
x = np.linspace(0, 11 * np.pi, 10000)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
fig.suptitle("""Butterfly Curve
        x = np.sin(x) * (np.exp(np.cos(x))- (2 * np.cos(4 * x)) - np.sin(x/12)**5)
        y = np.cos(x) * (np.exp(np.cos(x))- (2 * np.cos(4 * x)) - np.sin(x/12)**5)""", color='purple')

# Define the equations
def equation1(x):
    return np.sin(x) * (np.exp(np.cos(x)) - (2 * np.cos(4 * x)) - np.sin(x / 12) ** 5)

def equation2(x):
    return np.cos(x) * (np.exp(np.cos(x)) - (2 * np.cos(4 * x)) - np.sin(x / 12) ** 5)

# Compute the curve values
x1 = equation1(x)
y1 = equation2(x)

# Set axis limits and appearance
ax.set_xlim(min(x1), max(x1))
ax.set_ylim(min(y1) - 0.1, max(y1) + 0.2)
ax.set_facecolor("black")
ax.grid(True)

# Plot the initial line and the point
line, = ax.plot([], [], label='butterfly', lw=2, color='purple')
point, = ax.plot([], [], 'o', color='red')  # Adding the point marker

# Animation function
def animate(Frame):
    line.set_xdata(x1[:Frame])
    line.set_ydata(y1[:Frame])
    point.set_xdata(x1[Frame])
    point.set_ydata(y1[Frame])
    return [line, point]

# Create the animation
anime = FuncAnimation(fig, animate, frames=len(x), interval=0.001, blit=True)

# Show the plot
plt.show()
