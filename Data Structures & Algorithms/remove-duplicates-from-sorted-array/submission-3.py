class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # arrays of nums in non-decreasing order
        # rmv duplicates in-place, so elements appear once
        # return number of unique elements 

        L = R = 0
        n = len(nums)

        while R < n:
            # swap 
            nums[L] = nums[R]

            while R < n and nums[L] == nums[R]:
                R += 1

            # number of total pos. we swapped
            L += 1

        return L
