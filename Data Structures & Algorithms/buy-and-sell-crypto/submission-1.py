class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if len(prices) == 1:
            return 0
        l, r = 0, 1

        profit = 0
        while l < r and r < len(prices):
            profit = max(profit, (prices[r]-prices[l]))
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1
        return profit