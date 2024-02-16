import json
import time
import matplotlib.pyplot as plt

def binarySearch(array, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binarySearch(array, target, mid + 1, right)
    else:
        return binarySearch(array, target, left, mid - 1)

def timeSearch(array, task):
    length = len(array)
    midpoints = [
        0,
        length // 4,
        length // 2,
        3 * length // 4,
        length - 1
    ]
    minElapsed = float('inf')
    bestMidpoint = 0
    
    for midpoint in midpoints:
        startTime = time.time()
        result = binarySearch(array, task, 0, length - 1)
        endTime = time.time()
        elapsedTime = endTime - startTime
        if elapsedTime < minElapsed:
            minElapsed = elapsedTime
            bestMidpoint = midpoint
    
    return bestMidpoint

def loadData(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def main():
    searchTasks = loadData('ex7tasks.json')
    arrayData = loadData('ex7data.json')

    results = []
    for task in searchTasks:
        bestMidpoint = timeSearch(arrayData, task)
        results.append((task, bestMidpoint))

    tasks, midpoints = zip(*results)
    plt.scatter(tasks, midpoints, marker='o', c='green',)
    plt.xlabel('Search Task')
    plt.ylabel('Midpoint')
    plt.legend()
    plt.title('Interpolation Search')
    plt.show()



if __name__ == "__main__":
    main()

# Question 4:  
    # Based on the choice of the initial midpoint, the performance will improve
    # if the initial midpoint gets closer to the target value. So, the algorithm
    # will be better. But, when the initial midpoint becomes further from the target value,
    # it will take longer for binary search to converge, since the midpoint will be unfound until
    # it finally finds it. This then causes it to attempt more tries, thus taking longer.