def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

# For each index in the input list:
    # Set a j variable to the current index
    # While j is greater than 0 and the element at index j-1 is greater than the element at index j:
    # Swap the elements at indices j and j-1
    # Decrement j by 1
# Return the list
