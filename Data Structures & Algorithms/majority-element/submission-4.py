from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # a smarter way is using Boyer-Moore Algo 
        # see candidate, increment count, otherwise decrement 
        # count reach 0, pick a new candiate

        # works b/c the majority element appears more than half the
        # time; thus, it should survive the elimination process 

        candiate = None
        count = 0 

        for n in nums: 
            if count == 0:
                candiate = n
            
            count += (
                1 if candiate == n else -1
            )

        return candiate


        

    


        


        
        