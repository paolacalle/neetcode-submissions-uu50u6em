class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0 
        stack = []

        for i, h in enumerate(heights): 
            start = i
            while stack and stack[-1][1] > h:
                index, height= stack.pop()
                new_area = height * (i - index)
                area = max(
                    area, 
                    new_area
                )
                start = index
            stack.append((start, h))

        # handle case where the values extend the hist.
        n = len(heights)
        for i, h in stack:
            area = max(
                area, 
                h * (n - i)
            )
        
        return area






