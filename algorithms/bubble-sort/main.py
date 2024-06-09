def bubble_sort(nums):
    flag = True
    end = len(nums)
    while flag:
        flag = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                flag = True
        end -= 1
    return nums


# Procedure bubble_sort(nums):
#     Set swapping to True
#     Set end to the length of nums
#     While swapping is True:
#         Set swapping to False
#         For i from the 2nd element to end:
#             If the (i-1)th element of nums is greater than the ith element:
#                 Swap the (i-1)th element and the ith element of nums
#                 Set swapping to True
#         Reduce end by one
#     Return nums
# End Procedure
