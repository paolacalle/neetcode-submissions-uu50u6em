class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 = red; 1 = white; 2 = blue
        count = {
            0 : 0,
            1 : 0,
            2 : 0
        }

        for n in nums:
            count[n] += 1

        k = 0
        i = 0
        while k < 3:
            c = count[k] 

            if c != 0:
                nums[i] = k
                count[k] -= 1
                i += 1
            else:
                k += 1
        
        return nums
