class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Position - position of the ith car in miles
        Speed - speed of the ith car (miles per hour)
        Target - destination target miles


        Rules:
        -   Car cannot pass another ahead of it only catch up & 
            then driven at their speed.

        -   Car fleet: 
                - non-empty set of cars driving at the same 
                position and same speed. 

                - single car can be a car fleet

        Return (int) - number of different car fleets 
        """

        pairs = [
            (p, s)
            for p, s
            in sorted(
                zip(position, speed), 
                key=lambda x : x[0],
                reverse=True
            )
        ]

        stack = [] # keep track of arrival times
        
        for p, s in pairs: 
            stack.append((target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # found an arrival time that that is smaller
                # than the previous
                stack.pop()

        return len(stack)

            

        











