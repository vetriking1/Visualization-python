import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


fig,ax = plt.subplots(figsize=(10,7))

def equation(x, n, r):
    values = [x]
    for i in range(n):
        values.append(r * values[-1] * (1 - values[-1]))
    return values

n = 100
y_values = equation(0.4, n-1, 3.8)
x_values = [x for x in range(n)]

line, =ax.plot([],[],marker='.',lw=0.9,color='blue',markerfacecolor='purple',markeredgecolor='purple')
ax.set_xlim(0, n)
ax.set_ylim(min(y_values), max(y_values))
ax.set_title("Xn+1 = R*Xn*(1-Xn)\n r=3.8")
ax.set_xlabel("x")
ax.set_ylabel("y")
a_text = ax.text(0.5, 0.98, 'a = 0.0', 
                 ha='center', va='top', transform=ax.transAxes, fontsize=12)
def animate(frame):
    line.set_data(x_values[:frame],y_values[:frame])
    a_text.set_text("value = {}".format(y_values[frame]))
    return line,a_text
anime = FuncAnimation(fig, animate, frames=len(x_values), interval=10, blit=True)
# plt.plot(x_values,y_values)
plt.show()