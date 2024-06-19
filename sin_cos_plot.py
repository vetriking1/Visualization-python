import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate x values
x = np.linspace(0, 2 * np.pi, 1000)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)

# Initialize lines
line1, = ax.plot(x, np.sin(x), label='sin(x)',lw=2)
line2, = ax.plot(x, np.cos(x), label='cos(x)',color='red',lw=2)


# Add title and labels
ax.set_title('Animating Sine and Cosine waves')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)cos(x)')
ax.legend()
# ax.grid(True)

# Animation function
def animate(frame):
    line1.set_ydata(np.sin(x + frame / 10.0))  # Update y data
    line2.set_ydata(np.cos(x + frame / 10.0))
    return line1, line2

# Create animation
ani = FuncAnimation(fig, animate, frames=10000, interval=60, blit=True)

# Show animation
plt.show()
