class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 = red; 1 = white; 2 = blue
        count = [0] * 3
        for n in nums:
            count[n] += 1

        idx = 0
        for i in range(3):
            while count[i]:
                nums[idx] = i
                idx += 1
                count[i] -= 1
            
