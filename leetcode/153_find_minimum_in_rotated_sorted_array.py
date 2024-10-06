class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid
            
        return nums[l]