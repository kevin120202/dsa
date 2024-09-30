class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1

        return -1
