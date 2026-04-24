class Solution:
    # given an array
    # - sorted in ascending order 
    # - roated betwen 1 to n times 
    # - unique 

    # return the minimum elemnt of the array 
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # step # 1: find the split 
        while l < r: 
            m = l + (r - l) // 2

            # if the middle is greater than the right 
            # then the smallest number must be there
            if nums[m] > nums[r]:
                l = 1 + m 

            # if the middle is smaller than the left
            # than the smallest number must be at the left 
            else: 
                r = m

        return nums[l]

            




    # [3,4,5,6,1,2]
    # []
        
        