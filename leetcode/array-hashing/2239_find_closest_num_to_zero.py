class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for i in range(len(nums)):
            if abs(nums[i]) < abs(closest):
                closest = nums[i]
            elif abs(nums[i]) == abs(closest):
                if nums[i] > closest:
                    closest = nums[i]
        return closest
