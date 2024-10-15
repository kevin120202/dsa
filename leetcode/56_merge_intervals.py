class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=self.sort)
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]
        
        return res
    
    def sort(self, i):
        return i[0]