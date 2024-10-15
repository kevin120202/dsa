class Solution(object):
    def runningSum(self, nums):
        running_sum = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            running_sum.append(s)
        return running_sum
