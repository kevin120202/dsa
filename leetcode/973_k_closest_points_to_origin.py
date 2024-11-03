import heapq

class Solution(object):
    def kClosest(self, points, k):
        max_heap = []
        
        for point in points:
            x, y = point[0], point[1]
            dist = (x * x) + (y * y)

            heapq.heappush(max_heap, (-dist, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = []
        for point in max_heap:
            res.append(point[1])
        
        return res