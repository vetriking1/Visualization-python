import matplotlib.pyplot as plt
import numpy as np
from numba import cuda

# Set up the initial parameters
fig, ax = plt.subplots(figsize=(12, 12))

realX, imgY = -0.51, 0.52

@cuda.jit(device=True)
def julia_set_kernel(z, c, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

@cuda.jit
def draw_julia_set_kernel(x, y, c, max_iter, output):
    i, j = cuda.grid(2)
    if i < output.shape[0] and j < output.shape[1]:
        z = complex(x[j], y[i])
        output[i, j] = julia_set_kernel(z, c, max_iter)

def draw_julia_set(xmin, xmax, ymin, ymax, width, height, max_iter, c):
    x = np.linspace(xmin, xmax, width, dtype=np.float64)
    y = np.linspace(ymin, ymax, height, dtype=np.float64)
    
    d_x = cuda.to_device(x)
    d_y = cuda.to_device(y)
    d_output = cuda.device_array((height, width), dtype=np.float64)
    
    threads_per_block = (16, 16)
    blocks_per_grid_x = int(np.ceil(height / threads_per_block[0]))
    blocks_per_grid_y = int(np.ceil(width / threads_per_block[1]))
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)
    
    draw_julia_set_kernel[blocks_per_grid, threads_per_block](d_x, d_y, c, max_iter, d_output)
    
    output = d_output.copy_to_host()
    
    return output

# Draw the Julia set
image_m = draw_julia_set(-2.0, 2.0, -2.0, 2.0, 22000, 22000, 150, complex(realX, imgY))

# Display the Julia set as a heatmap
im = ax.imshow(image_m, extent=(-2.0, 2.0, -2.0, 2.0), cmap='viridis', interpolation="none")
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_title('Julia Set')

# Save the high-resolution image
print("Saved high-resolution image as juliaset.png")
plt.savefig('juliaset.png', dpi=1500, bbox_inches='tight')
