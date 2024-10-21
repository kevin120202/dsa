class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        wind = set()
        l = 0
        for r in range(len(nums)):
            if (r - l) > k:
                wind.remove(nums[l])
                l += 1
            if nums[r] in wind:
                return True

            wind.add(nums[r])
        
        return False