class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in range(len(piles)):
                hours += (piles[i] + (k-1)) // k
            if hours <= h:
                r = k - 1
            else:
                l = k + 1
        
        return l