# Randomized QuickSort
# Chooses a random pivot each time

import random

def partition_random(arr, low, high):
    pivot_index = random.randint(low, high)   # choose random pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort_random(arr, low, high):
    if low < high:
        pi = partition_random(arr, low, high)
        quicksort_random(arr, low, pi - 1)
        quicksort_random(arr, pi + 1, high)


# --- Main program ---
arr = [10, 7, 8, 9, 1, 5]
print("Original Array:", arr)

quicksort_random(arr, 0, len(arr) - 1)
print("Sorted Array (Randomized QuickSort):", arr)
