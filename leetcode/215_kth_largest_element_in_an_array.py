import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)