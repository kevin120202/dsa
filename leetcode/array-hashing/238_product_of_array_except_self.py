class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)  # [1,1,1,1]
        pre = 1
        for i, num in enumerate(nums):
            res[i] = pre
            pre *= num

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res
