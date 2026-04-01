class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1


        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[-1] = height[-1]
        for i in range(1, n):
            rightMax[-1 * i] = max(rightMax[-1 * i + 1], height[-1 * i])

        # o(n)
        area = 0
        for i in range(n):
            if leftMax[i] == 0:
                continue

            a = min(leftMax[i], rightMax[i]) - height[i]

            if a <= 0:
                continue

            area += a

        return area


            


            
            

            

            

            



                





        

        