def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False


# Set low = 0 and high = n - 1.
# While low <= high:
    # Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
    # If array[median] == target, return True
    # Else if array[median] < target, set low to median + 1
    # Otherwise set high to median - 1
# Return False
