import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
    
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            diff = largest - next_largest
            if diff != 0:
                heapq.heappush(stones, diff)
        
        if len(stones) == 1:
            return -heapq.heappop(stones)
        return 0