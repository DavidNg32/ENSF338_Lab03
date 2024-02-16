import random
import time
import matplotlib.pyplot as plt

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binarySearch(arr, key, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid
    return start

def sortBinaryInsert(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binarySearch(arr, key, 0, i)
        arr[j+1:i+1] = arr[j:i]
        arr[j] = key

def genInput(length):
    return [random.randint(0, 1000) for _ in range(length)]

def testAlgorithm(algorithm, input_lengths):
    executionTimes = []
    for length in input_lengths:
        input_array = genInput(length)
        
        start_time = time.time()
        algorithm(input_array)
        end_time = time.time()
        
        timeExe = end_time - start_time
        executionTimes.append(timeExe)
        print(f"Length: {length}, Execution Time: {timeExe:.10f} seconds")
    
    return executionTimes

if __name__ == "__main__":
    print("********************************************************\n")
    inputLengths = [100, 200, 300, 400, 500]
    print("Testing Traditional Insertion Sort:")
    insertionTimes = testAlgorithm(insertionSort, inputLengths)
    
    print("\nTesting Binary Insertion Sort:")
    binaryTimes = testAlgorithm(sortBinaryInsert, inputLengths)
    print("\n********************************************************\n")

    # Plotting
    plt.plot(inputLengths, insertionTimes, label='Insertion Sort')
    plt.plot(inputLengths, binaryTimes, label='Binary Insertion Sort')
    plt.xlabel('Input Length')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Insertion Sort Algorithms')
    plt.legend()
    plt.show()

# Question 4:
# Based on the graph, and the results of our output message, binary search is generally more faster as the input sizes grows,
# because it stays at a consistent number while the traditional way actually increases in seconds adhering to the formula O(n)
# as shown from the graph. In regards to binary search with a time complexity of O(log n), the average case peformance is faster
# and better as an algorithm when the input sizes are large in number.