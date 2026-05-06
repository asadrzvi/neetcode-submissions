class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r, i, j = 0, 0, 1
        max_p = 0
        while r < len(prices):
            if prices[i] < prices[r]:
                profit = prices[r] - prices[i]
                max_p = max(max_p, profit)
            else:
                i = r
            r+=1
        return max_p
                


