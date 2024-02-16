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

def measureMe(search_function, input_size, num_trials=10):
    arr = np.random.randint(0, 1000, input_size)
    target_list = np.random.choice(arr, 100)  

    total_time = 0
    for target in target_list:
        for _ in range(num_trials):
            start_time = time.time()
            index = search_function(arr, target)
            end_time = time.time()
            total_time += end_time - start_time

    averageTime = total_time / (num_trials * 100)

    if index != -1:
        print(f"Avg. time to find targets using {search_function.__name__} with input size {input_size}: {averageTime:.10f} seconds")
    else:
        print(f"Targets not found. Avg. time: {averageTime:.10f} seconds")
    
    return averageTime

def main():
    input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

    linear_times = []
    binary_times = []
    for size in input_sizes:
        linear_time = measureMe(linearSearch, size)
        binary_time = measureMe(quickBinary, size)
        linear_times.append(linear_time)
        binary_times.append(binary_time)

    plt.plot(input_sizes, linear_times, label='Linear Search')
    plt.plot(input_sizes, binary_times, label='Binary Search with Quicksort')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Performance of Search Algorithms on 100 Random Tasks')
    plt.legend()
    plt.show()

print("*************************************************************************************************************\n")
main()
print("\n*************************************************************************************************************\n")

# Question 4 Discussion
# Upon plotting the average times, we can see that quick search with binary takes more time and increaces as the input size goes up while
# linear search stays fairly consistent and faster in contrast. Based on our results, linear search stays around the same time and doesn't get longer often, suggesting that it maintains a relatively constant time complexity, likely linear (O(n)).
# But, binary quicksory actually gets longer in time as the input size grows. This most likely to the nature of the sort when it goes through large amounts of data.
