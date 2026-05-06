class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_p = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                if max_p < profit:
                    max_p = profit
            else:
                i = j
            j+=1
        return max_p
                


