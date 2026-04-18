from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = defaultdict(int)
        n = len(nums)

        for i in nums:
            counts[i] += 1

            if counts[i] >= n / 2:
                return i

        

    


        


        
        