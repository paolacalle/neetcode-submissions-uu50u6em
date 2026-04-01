from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Assumption:
        - every input has exactly one pair of indices i and j

        Return 
        - i and j such that i != j 
        - nums[i] + nums[j] == target
        """
        j_num_needed = {i : target - i_num for i, i_num in enumerate(nums)}

        j_num_pos = defaultdict(int)
        for j_pos, j_value in enumerate(nums):
            j_num_pos[j_value] = j_pos

        for i in j_num_needed.keys():
            j_needed = j_num_needed[i]
            j = j_num_pos[j_needed]
            
            if i < j:
                return [i, j]





        

        



        
        