def merge_sort(nums):
    if len(nums) < 2:
        return nums
    left_side = nums[:len(nums) // 2]
    right_side = nums[len(nums) // 2:]
    sorted_left = merge_sort(left_side)
    sorted_right = merge_sort(right_side)
    return merge(sorted_left, sorted_right)


# MERGE_SORT()
# If the length of A is less than 2, it's already sorted so return it
# Split the input array into two halves down the middle
# Call merge_sort() twice, once on each half
# Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final


# MERGE() IMPLEMENTATION

# Create a new "final" list of integers.
# Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
# Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
# After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other). Add those extra items to the final list.
# Return the final list.
