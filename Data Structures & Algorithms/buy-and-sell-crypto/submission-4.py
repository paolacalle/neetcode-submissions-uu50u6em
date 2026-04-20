class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_idx = 0

        for i in range(1, len(prices)):
            p = prices[i] - prices[buy_idx]

            if prices[i] < prices[buy_idx]:
                buy_idx = i

            profit = max(profit, p)
            
        return profit


