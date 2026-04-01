class Solution:
    # non-negative integers height --> elevation map 
    # height[i] --> height of bar
    # width = 1

    # max are of water that can be trapped between bars

    # time = o(n)

    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1

        prefix = []
        suffix = []

        curr_max = 0
        while l < n:
            prefix.append(curr_max)
            curr_max = max(curr_max, height[l])
            l += 1

        curr_max = 0
        while r > -1:
            suffix.insert(0, curr_max)
            curr_max = max(curr_max, height[r])
            r -= 1

        area = 0
        for i in range(n):
            if prefix[i] == 0:
                continue

            a = min(prefix[i], suffix[i]) - height[i]

            if a <= 0:
                continue

            area += a

        return area


            


            
            

            

            

            



                





        

        