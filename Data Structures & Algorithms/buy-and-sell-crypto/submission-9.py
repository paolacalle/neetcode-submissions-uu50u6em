class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # same idea cleaner code
        max_p = 0
        min_b = prices[0]

        # one extra iteration, but slicing and range is still 
        # slightly more expensive, thus cheaper to do the 
        # reduandant step
        for sell in prices:
            max_p = max(max_p, sell - min_b)
            min_b = min(min_b, sell)
            
        return max_p


