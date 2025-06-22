from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        res = float('inf')
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                closeness = abs(curr_sum - target)
                if closeness < closest_sum:
                    closest_sum = closeness
                    res = curr_sum
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    return curr_sum
        return res