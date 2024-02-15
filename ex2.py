import time
import random
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def test_sorting_algorithms():
    sizes = [i*100 for i in range(1, 21)]  # Sizes from 100 to 2000
    scenarios = ['best', 'worst', 'average']
    times = {'bubble': {scenario: [] for scenario in scenarios}, 'quick': {scenario: [] for scenario in scenarios}}

    plt.figure(figsize=(10, 5))  # Create a single plot figure

    for scenario in scenarios:
        for size in sizes:
            if scenario == 'best':
                arr = list(range(size))
            elif scenario == 'worst':
                arr = list(range(size, 0, -1))
            else:  # scenario == 'average'
                arr = list(np.random.randint(1, 1000, size=size))

            start = time.time()
            bubble_sort(arr.copy())
            end = time.time()
            times['bubble'][scenario].append(end - start)

            start = time.time()
            quick_sort(arr.copy(), 0, len(arr) - 1)
            end = time.time()
            times['quick'][scenario].append(end - start)

        # Plot the times for each scenario without creating a new figure
        plt.plot(sizes, times['bubble'][scenario], label=f'Bubble Sort ({scenario.capitalize()} Case)')
        plt.plot(sizes, times['quick'][scenario], label=f'Quick Sort ({scenario.capitalize()} Case)')

    # Determine threshold
    for size in sizes:
        if times['bubble']['average'][-1] > times['quick']['average'][-1]:
            threshold = size
            break

    # Add a vertical line at the threshold value
    plt.axvline(x=threshold, color='r', linestyle='--', label='Threshold')

    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance of Bubble Sort vs Quick Sort')
    plt.legend()
    plt.grid(True)
    plt.show()  # Show the plot after the loop

    print("Chosen threshold:", threshold)

test_sorting_algorithms()