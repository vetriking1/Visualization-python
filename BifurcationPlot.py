import matplotlib.pyplot as plt
import numpy as np

def equation(x, n, r):
    values = [x]
    for i in range(n):
        values.append(r * values[-1] * (1 - values[-1]))
    return values[-100:]  # Return the last 100 values to focus on steady-state behavior

# Initialize parameters
initial_x = 0.4
iterations = 500
r_values = np.linspace(1, 4, 1000)  # Fine-grained range for the bifurcation diagram
x_values = []

# Calculate the logistic map for each r
for r in r_values:
    final_values = equation(initial_x, iterations, r)
    for value in final_values:
        x_values.append((r, value))

# Convert to numpy array for easy plotting
x_values = np.array(x_values)

# Plot the bifurcation diagram
plt.figure(figsize=(10, 7))
plt.plot(x_values[:, 0], x_values[:, 1], 'k.', markersize=0.8,color='blue')
plt.title("Bifurcation Diagram of the Logistic Map")
plt.xlabel("Parameter r")
plt.ylabel("x")
plt.grid(True)
plt.show()
