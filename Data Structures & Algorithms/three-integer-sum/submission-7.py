class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []

        for i in range(n):
            numi = nums[i]

            # edge case: all remaining numbers are postive
            if numi > 0: 
                break

            # this number has already been proccesed
            if i > 0 and numi == nums[i - 1]:
                continue 

            # l is one above i 
            # r is always at the end
            l, r = i + 1, n - 1

            while l < r:
                s = numi + nums[l] + nums[r]

                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    output.append([numi, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # skip duplicates for the third number
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        # take care of dups
        return output