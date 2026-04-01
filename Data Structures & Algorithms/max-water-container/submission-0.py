class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)    
        area = 0
        l, r = 0, n - 1

        while l < r:
            w = r - l 
            h = min(heights[l], heights[r])
            area = max(area, w * h)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return area






        