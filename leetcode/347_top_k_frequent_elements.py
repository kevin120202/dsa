import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        min_heap = []
        for num in freq:
            item = (freq[num], num)
            heapq.heappush(min_heap, item)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])        
        
        return res