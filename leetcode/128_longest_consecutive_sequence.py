class Solution(object):
    def longestConsecutive(self, nums):
        sett = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in sett:
                length = 0
                while nums[i] + length in sett:
                    length += 1
                longest = max(length, longest)
            
        return longest