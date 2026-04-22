class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # intialize 
        area, stack = 0, []

        # iterate 
        for i, h in enumerate(heights): 
            # start keeps track of how far our current 
            # height can extend out (width wise)
            start = i
            while stack and stack[-1][1] > h:
                # if it is greater, then it can not be further 
                # extended to the right as it will always be limited 
                # by the this smaller height ahead of it 
                index, height= stack.pop()

                # calculate the max area this height was able to 
                # produce. 
                #   - The end point is i since it is the point it 
                #.    can no longer extend to the right 
                #   - The start point is index as this is where 
                #.    this height begins to take over 
                new_area = height * (i - index)

                # update the max-height pointer
                area = max(
                    area, 
                    new_area
                )

                # the new height start is the height we just popped 
                # end point
                start = index

            # push onto stack
            stack.append((start, h))

        # handle case where the values extend the entire hist.
        n = len(heights)
        for i, h in stack:
            # simply iterate the stack
            # and update the max
            area = max(
                area, 
                h * (n - i) # since end is the end of list
            )
        
        return area

# time-compleity : O(n)
# - Iterates through each of the heights once
# - Pops once
# - appends once

# space-complexity : O(n)
# - in the worst case, we have the entire elements in the stack 








