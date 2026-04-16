class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # arrays of nums in non-decreasing order
        # rmv duplicates in-place, so elements appear once
        # return number of unique elements 

        # pass one replace dups
        j = 0
        curr = nums[j]
        noneIndx = []
        while j < len(nums) - 1:
            curr = nums[j]
            if nums[j + 1] == curr:
                nums[j] = None
                noneIndx.append(j)
            else:
                curr = nums[j + 1]

            j += 1

        # remove none
        while noneIndx:
            idx = noneIndx.pop(-1)
            nums.pop(idx)

        return len(nums)
