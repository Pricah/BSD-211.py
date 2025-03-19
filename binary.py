def binary_search(arr, target):
    """Perform binary search for the target in a sorted array."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid  # Return the index if found

        # If the target is smaller than mid, it must be in the left half
        elif arr[mid] > target:
            right = mid - 1

        # If the target is larger than mid, it must be in the right half
        else:
            left = mid + 1

    return -1  # Return -1 if the target is not found


# example searchimg for number3 in an array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Sorted array
target = 3

# Perform binary search
result = binary_search(arr, target)

# Output the result
if result != -1:
    print(f"Number {target} found at index {result}.")
else:
    print(f"Number {target} not found in the array.")
