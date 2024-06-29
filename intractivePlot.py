import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)  # Adjust the bottom space to fit three sliders

def equation(x, n, r):
    values = [x]
    for i in range(n):
        values.append(r * values[-1] * (1 - values[-1]))
    return values

n = 100
initial_value = 0.4
ratio = 3.8

# Create slider axes below the main plot
ax_slider_ratio = plt.axes([0.1, 0.25, 0.8, 0.03])  # [left, bottom, width, height]
ax_slider_initial_value = plt.axes([0.1, 0.15, 0.8, 0.03])  # [left, bottom, width, height]
ax_slider_n = plt.axes([0.1, 0.05, 0.8, 0.03])  # [left, bottom, width, height]

slider_ratio = Slider(ax_slider_ratio, "ratio(r)", valmin=1, valmax=4, valinit=ratio)
slider_initial_value = Slider(ax_slider_initial_value, "initial_value(x)", valmin=0, valmax=1, valinit=initial_value)
slider_n = Slider(ax_slider_n, "number of iteration(n)", valmin=1, valmax=2000, valinit=n, valstep=1)

def update(val):
    r = slider_ratio.val
    x0 = slider_initial_value.val
    n = int(slider_n.val)
    y_values = equation(x0, n-1, r)
    line.set_ydata(y_values)
    line.set_xdata(range(n))
    ax.set_xlim(0, n)
    ax.set_ylim(0, max(y_values))  # Adjust y-limit to fit new values
    fig.canvas.draw_idle()

slider_ratio.on_changed(update)
slider_initial_value.on_changed(update)
slider_n.on_changed(update)

y_values = equation(initial_value, n-1, ratio)
x_values = range(n)

line, = ax.plot(x_values, y_values, marker='o', lw=1.2, color='blue', markerfacecolor='purple', markeredgecolor='purple')
ax.set_xlim(0, n)
ax.set_ylim(0, 1)  # Set y-limit to [0, 1]
ax.set_title("Xn+1 = R*Xn*(1-Xn)")
ax.set_xlabel("n")
ax.set_ylabel("Xn")

plt.show()
