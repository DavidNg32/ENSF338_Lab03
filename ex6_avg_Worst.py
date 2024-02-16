import numpy as np
import time
import matplotlib.pyplot as plt

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def quickBinary(arr, target):
    sorted_arr = quicksort(arr)
    return binarySearch(sorted_arr, target)


def measureMeWorst(search_function, input_size, num_trials=10):
    arr = np.arange(input_size)  # Generate a sorted array
    target_list = np.random.choice(arr, 100)

    total_time = 0
    for target in target_list:
        for _ in range(num_trials):
            start_time = time.time()
            index = search_function(arr, target)
            end_time = time.time()
            total_time += end_time - start_time

    average_time = total_time / (num_trials * 100)

    if index != -1:
        print(f"Avg. time to find targets using {search_function.__name__} with input size {input_size}: {average_time:.10f} seconds")
    else:
        print(f"Targets not found. Avg. time: {average_time:.10f} seconds")

    return average_time


def reverseArray(size):
    return list(range(size, 0, -1))

def main():
    input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

    linear_times = []
    binary_times = []
    for size in input_sizes:
        linear_time = measureMeWorst(linearSearch, size)
        binary_time = measureMeWorst(quickBinary, size)
        linear_times.append(linear_time)
        binary_times.append(binary_time)

    plt.plot(input_sizes, linear_times, label='Linear Search')
    plt.plot(input_sizes, binary_times, label='Binary Search with Quicksort')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Performance of Search Algorithms on Reverse Sorted Arrays')
    plt.legend()
    plt.show()

print("*************************************************************************************************************\n")
main()
print("\n*************************************************************************************************************\n")


# Question 5 Discussion
