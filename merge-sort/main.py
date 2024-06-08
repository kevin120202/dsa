def merge_sort(nums):
    if len(nums) < 2:
        return nums
    left_side = nums[:len(nums) // 2]
    right_side = nums[len(nums) // 2:]
    sorted_left = merge_sort(left_side)
    sorted_right = merge_sort(right_side)
    return merge(sorted_left, sorted_right)


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
