def linear_search(arr, target):
    """Perform a linear search for the target in the array."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# example
arr = [5, 3, 8, 6, 7, 3, 2, 4, 3]
target = 3

# Perform linear search
result = linear_search(arr, target)

# Output the result
if result != -1:
    print(f"Number {target} found at index {result}.")
else:
    print(f"Number {target} not found in the array.")
