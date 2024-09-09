class Solution:
    def sortedSquares(self, nums):
        res = []

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] > nums[r]:
                res.append(nums[l])
                l += 1
            else:
                res.append(nums[r])
                r -= 1

        res.reverse()

        return res
