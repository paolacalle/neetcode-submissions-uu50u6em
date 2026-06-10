import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r: 
            k = (l + r) // 2
            
            # calculate the hours consumed
            total_hours = 0 
            for p in piles:
                total_hours += math.ceil(p / k)

            if total_hours <= h: 
                # try to find a smaller number
                res = k
                r = k - 1
            else:
                # try to find a bigger number
                l = k + 1

        return res
            

