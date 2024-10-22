class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        r = 0
        curr_sum = 0
        res = float('inf')
        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= target:
                curr_sum -= nums[l]
                res = min(res, r - l + 1)
                l += 1

            r += 1

        return res if res != float('inf') else 0