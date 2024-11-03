import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        count = {}
        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1
        
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = []

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.pop(0)[0])
        
        return time