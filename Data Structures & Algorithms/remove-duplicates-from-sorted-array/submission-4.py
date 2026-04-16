class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # arrays of nums in non-decreasing order
        # rmv duplicates in-place, so elements appear once
        # return number of unique elements 

        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l
