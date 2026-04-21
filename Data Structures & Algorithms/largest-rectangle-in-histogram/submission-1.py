class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # area = width * height
        # height = smallest height otherwise will span out of the area
        # width = distance between = r - l + 1
        n = len(heights)
        left = [-1] * n
        right = [n] * n # make the deafult the max distance


        # the idea here is that for each position 
        # determine what is the smallest height 
        # from the left & right side
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack: 
                right[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack: 
                left[i] = stack[-1]
            stack.append(i)

        print(right, left)
        area = -1
        for i in range(n):
            # narrow down window 
            left[i] += 1
            right[i] -= 1
            window_size = (right[i] - left[i] + 1)

            area = max(
                area, 
                heights[i] * window_size
            )

    
        print(area)
        return area






