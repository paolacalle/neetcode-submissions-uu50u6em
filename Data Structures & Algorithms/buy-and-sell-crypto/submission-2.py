class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
    # 10, 1, 5, 6, 7, 1
    # 10, 1 = -9
    # 1, 5 = 4
    # 1, 6 = 5 vs 5, 6 = 1
    # 1, 7 = 6 vs 6, 7 = 1
    # 1, 1 = 0 vs. 7, 1 = -6

        profit = 0
        buy_idx = 0

        for i in range(0, len(prices)):
            p = prices[i] - prices[buy_idx]

            if prices[i] < prices[buy_idx]:
                buy_idx = i

            profit = max(profit, p)
            

        return profit


