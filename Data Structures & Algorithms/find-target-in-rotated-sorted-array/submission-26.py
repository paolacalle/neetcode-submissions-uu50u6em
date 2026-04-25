class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r  = 0, len(nums) - 1
        while l <= r: 
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m

            if nums[m] > nums[r]:
                # this means that there exists a 
                # lower number 
                # to the right
                if nums[m] > target and nums[l] <= target : 
                    r = m - 1
                else: 
                    l = m + 1
            
            else:
               # check the target number
               # to determine which way to go 
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                elif nums[m] <= target and target <= nums[r]:
                    l = m + 1
                elif nums[l] <= target:
                    r = m - 1
                elif nums[r] <= target:
                    l = m + 1
                else:
                    if nums[m] < target:
                        l = m + 1
                    else: 
                        r = m - 1
        return -1 

            

# [4,5,6,7,0,1,2]
# target = 0 






