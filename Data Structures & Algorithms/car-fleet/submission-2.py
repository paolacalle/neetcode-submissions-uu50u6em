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

        idx_pos = [
            (p, s)
            for p, s
            in sorted(zip(position, speed), key=lambda x : x[0])
        ]

        ahead_pos, ahead_speed = idx_pos.pop(-1)
        prev_t = (target - ahead_pos) / ahead_speed

        fleets = 1
        while idx_pos: 
            p, s = idx_pos.pop(-1)
            curr_t = (target - p) / s

            if curr_t > prev_t: 
                prev_t = curr_t
                fleets += 1

        return fleets

            

        











