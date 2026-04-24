class Solution:
    # given an array
    # - sorted in ascending order 
    # - roated betwen 1 to n times 
    # - unique 

    # return the minimum elemnt of the array 
    def findMin(self, nums: List[int]) -> int:
        # brute force
        return min(nums)
        