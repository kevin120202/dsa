class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            r += 1
        return profit
