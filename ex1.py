import sys;

sys.setrecursionlimit(20000)


def merge(arr, low, mid, high):
    # Create two temporary arrays to hold the two halves
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    # Initialize indices for left, right and merged subarray
    i = j = 0
    k = low

    # Merge the temp arrays back into arr[low..high]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of left[], if there are any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of right[], if there are any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
    return arr
