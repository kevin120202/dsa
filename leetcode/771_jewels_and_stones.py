class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels_set = set(jewels)  
        res = 0
        for char in stones:
            if char in jewels_set:
                res += 1
        
        return res