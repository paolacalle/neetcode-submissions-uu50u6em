class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r  = 0, len(nums) - 1
        while l <= r: 
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m

            if nums[m] > nums[r]:
                # right-side has smaller numbers
                if target >= nums[l] and target < nums[m]:
                    # check the left-side of the array 
                    # b/c the numbers are bigger 
                    # on the left than the right
                    r = m - 1
                else: 
                    # check the right-side
                    # b/c the numbers are smaller
                    # on the left than the right
                    l = m + 1
            
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1



        return -1 

            




