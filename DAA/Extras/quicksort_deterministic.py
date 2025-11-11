# Deterministic QuickSort
# Always picks the last element as the pivot

def partition(arr, low, high):
    pivot = arr[high]      # last element as pivot
    i = low - 1            # pointer for smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort_deterministic(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_deterministic(arr, low, pi - 1)
        quicksort_deterministic(arr, pi + 1, high)


# --- Main program ---
arr = [10, 7, 8, 9, 1, 5]
print("Original Array:", arr)

quicksort_deterministic(arr, 0, len(arr) - 1)
print("Sorted Array (Deterministic QuickSort):", arr)
