import timeit

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

for n in range(10, 200, 10):
    arr = list(range(n, 0, -1))

    start = timeit.default_timer()
    newarr = quicksort(arr, 0, len(arr)-1)
    stop = timeit.default_timer()

    print(f"For n = {n},  it took {stop-start:.6f} to quicksort.")