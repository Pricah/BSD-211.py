def quick_sort(arr):
    """Sort the array using quick sort."""
    if len(arr) <= 1:
        return arr  # Base case: single-element or empty array is already sorted

    # Select pivot (in this case, we use the last element as pivot)
    pivot = arr[-1]

    # Partition the array into two sub-arrays
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort the left and right sub-arrays and combine with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)


# example
arr = [38, 15, 41, 39, 42]
sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)
