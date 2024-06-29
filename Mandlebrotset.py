import matplotlib.pyplot as plt
import numpy as np
import time

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    
    mandelbrot_set_values = np.zeros((height, width))
    
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mandelbrot_set_values[i, j] = mandelbrot(c, max_iter)
    
    return mandelbrot_set_values

start_time = time.time()

image_m = draw_mandelbrot(-2.0, 1.0, -1.5, 1.5, 1000, 1000, 200)

# Create image plot
plt.figure(figsize=(10, 10))
plt.imshow(image_m, cmap='viridis', extent=(-2.0, 1.0, -1.5, 1.5))
plt.colorbar()
plt.xlim(-2.0, 1.0)
plt.ylim(-1.5, 1.5)
plt.xlabel('Re')
plt.ylabel('Im')
plt.title('Mandelbrot Set')

print(f"{time.time() - start_time:.2f} seconds")


plt.show()
