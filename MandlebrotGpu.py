import matplotlib.pyplot as plt
import numpy as np
from numba import cuda, jit
import time

@cuda.jit(device=True)
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

@cuda.jit
def mandelbrot_kernel(d_x, d_y, d_output, max_iter):
    i, j = cuda.grid(2)
    if i < d_output.shape[0] and j < d_output.shape[1]:
        c = complex(d_x[j], d_y[i])
        d_output[i, j] = mandelbrot(c, max_iter)

def draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width, dtype=np.float64)
    y = np.linspace(ymin, ymax, height, dtype=np.float64)
    
    # Transferring data to GPU memory
    d_x = cuda.to_device(x)
    d_y = cuda.to_device(y)
    d_output = cuda.device_array((height, width), dtype=np.float64)
    
    # Defining the block and grid dimensions
    threads_per_block = (16, 16)
    blocks_per_grid_x = int(np.ceil(height / threads_per_block[0]))
    blocks_per_grid_y = int(np.ceil(width / threads_per_block[1]))
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)
    
    # Launching the kernel
    mandelbrot_kernel[blocks_per_grid, threads_per_block](d_x, d_y, d_output, max_iter)
    
    # Copying the result back to host memory
    mandelbrot_set_values = d_output.copy_to_host()
    
    return mandelbrot_set_values

start_time = time.time()

image_m = draw_mandelbrot(-2.0, 1.0, -1.5, 1.5, 21000, 21000, 200)


# image plot
plt.figure(figsize=(10, 10))
plt.imshow(image_m, extent=(-2.0, 1.0, -1.5, 1.5), cmap='viridis')
# plt.colorbar()
plt.xlim(-2.0, 1.0)
plt.ylim(-1.5, 1.5)
plt.xlabel('Re')
plt.ylabel('Im')
plt.title('Mandelbrot Set')
print(f"{time.time() - start_time:.2f} seconds1")
plt.savefig('MandleBrotsetHighRes.png', dpi=2000, bbox_inches='tight')
print(f"{time.time() - start_time:.2f} seconds2")
# plt.show()

