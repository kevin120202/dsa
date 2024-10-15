class Solution(object):
    def majorityElement(self, nums):
        ans = -1
        count = 0
        for num in nums:
            if count == 0:
                ans = num
            if ans != num:
                count -= 1
            else:
                count += 1
        
        return ans