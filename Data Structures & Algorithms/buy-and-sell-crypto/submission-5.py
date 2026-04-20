class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # same idea cleaner code
        max_p = 0
        min_b = prices[0]

        for sell in prices[1:]:
            max_p = max(max_p, sell - min_b)
            min_b = min(min_b, sell)
            
        return max_p


