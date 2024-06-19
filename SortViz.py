"""Created using help of Ai - created by <Vetri Selvan M>"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# import matplotlib
#for optimization
# matplotlib.use('TkAgg')

# Function to update the plot
def draw_data(ax, data, color_array, title):
    ax.cla()
    ax.bar(range(len(data)), data, color=color_array)
    ax.set_title(title)
    ax.set_xlim(-1, len(data))
    ax.set_ylim(-1, max(data) + 10)  # Adjusted to provide some margin for better visualization
    ax.set_yticks([])  # Adjusted y-axis ticks
    ax.set_xticks([])  # Adjusted y-axis ticks
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

# Bubble Sort generator
def bubble_sort_gen(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            yield data, ['blue' if x != j and x != j + 1 else 'red' for x in range(len(data))]
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        yield data, ['green' if x >= n - i - 1 else 'blue' for x in range(len(data))]
    yield data, ['green' for x in range(len(data))]

# Selection Sort generator
def selection_sort_gen(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            yield data, ['blue' if x != j and x != min_idx else 'red' for x in range(len(data))]
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        yield data, ['green' if x <= i else 'blue' for x in range(len(data))]
    yield data, ['green' for x in range(len(data))]

# Heap Sort generator
def heap_sort_gen(data):
    def heapify(data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Highlight current nodes being compared
        yield data, ['blue' if x != i else 'red' for x in range(len(data))]
        if left < n:
            yield data, ['blue' if x != left else 'red' for x in range(len(data))]
        if right < n:
            yield data, ['blue' if x != right else 'red' for x in range(len(data))]

        # Max-heapify subtree
        if left < n and data[i] < data[left]:
            largest = left

        if right < n and data[largest] < data[right]:
            largest = right

        # Swap and continue heapifying if necessary
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            yield from heapify(data, n, largest)

    n = len(data)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(data, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        yield data, ['green' if x == i else 'blue' for x in range(len(data))]
        yield from heapify(data, i, 0)

    yield data, ['green' for _ in range(len(data))]

# Insertion Sort generator
def insertion_sort_gen(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            yield data, ['blue' if x != j and x != j + 1 else 'red' for x in range(len(data))]
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        yield data, ['green' if x <= i else 'blue' for x in range(len(data))]
    yield data, ['green' for x in range(len(data))]

# Quick Sort generator
def quick_sort_gen(data):
    def quick_sort_recursive(data, low, high):
        if low < high:
            pi = yield from partition(data, low, high)
            yield from quick_sort_recursive(data, low, pi - 1)
            yield from quick_sort_recursive(data, pi + 1, high)

    def partition(data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            yield data, ['blue' if x != j and x != high else 'red' for x in range(len(data))]
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        yield data, ['green' if x == i + 1 or x == high else 'blue' for x in range(len(data))]
        return i + 1

    yield from quick_sort_recursive(data, 0, len(data) - 1)
    yield data, ['green' for x in range(len(data))]



# Radix Sort generator
def radix_sort_gen(data):
    def counting_sort(data, exp):
        n = len(data)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = data[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = data[i] // exp
            output[count[index % 10] - 1] = data[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(len(data)):
            data[i] = output[i]
            yield data, ['blue' if x != i else 'red' for x in range(len(data))]

    max_val = max(data)
    exp = 1
    while max_val // exp > 0:
        yield from counting_sort(data, exp)
        exp *= 10
    yield data, ['green' for x in range(len(data))]

# Main visualization function
def visualize_sorts():
    size = 50
    data = np.random.randint(1, 100, size)
    fig, axs = plt.subplots(3, 2, figsize=(15, 15))
    axs = axs.flatten()
    # fig.set_facecolor('black')
    sortNames = ['Bubble Sort', 'Selection Sort', 'Heap Sort', 'Insertion Sort', 'Quick Sort', 'Radix Sort']
    for i in range(len(sortNames)):
        axs[i].set_facecolor('black')
        axs[i].set_title(sortNames[i],color='purple')
    # Copy data for each sorting algorithm
    data_bubble = data.copy()
    data_selection = data.copy()
    data_heap = data.copy()
    data_insertion = data.copy()
    data_quick = data.copy()
    data_radix = data.copy()

    # Create generators for each sorting algorithm
    generators = [
        bubble_sort_gen(data_bubble),
        selection_sort_gen(data_selection),
        heap_sort_gen(data_heap),
        insertion_sort_gen(data_insertion),
        quick_sort_gen(data_quick),
        radix_sort_gen(data_radix),
    ]

    def update(frame):
        for ax, gen in zip(axs, generators):
            try:
                data, color_array = next(gen)
                draw_data(ax, data, color_array, ax.get_title())
            except StopIteration:
                continue

    anim = FuncAnimation(fig, update, frames=range(size * size),interval=10, repeat=False)
    plt.show()

if __name__ == "__main__":
    visualize_sorts()
