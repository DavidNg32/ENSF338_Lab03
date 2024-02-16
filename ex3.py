import random

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps

def generate_random_list(n):
    return [random.randint(0, 100) for _ in range(n)]

for n in range(10, 101, 10):
    arr = generate_random_list(n)
    sorted_arr, comparisons, swaps = bubble_sort(arr)
    print(f"For n = {n}, number of comparisons: {comparisons}, number of swaps: {swaps}")