class Solution(object):
    def sortColors(self, nums):
        start = 0
        curr = 0
        end = len(nums) - 1
        while curr <= end:
            if nums[curr] == 0:
                nums[curr], nums[start] = nums[start], nums[curr]
                start += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1
                
        return nums