class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1] * n
        left = [1] * n 

        # populate the right
        # o(n)
        for i in range(1, n):
            prev_right = right[i - 1]
            prev_num = nums[i - 1]
            curr_product = prev_right * prev_num
            right[i] = curr_product

        # populate the left
        # O(n)
        for i in range(n - 2, -1, -1):
            prev_left = left[i + 1]
            prev_num = nums[i + 1]
            curr_product = prev_left * prev_num
            left[i] = curr_product

        # print(f"left : {left}, right: {right}")

        # calculate the result
        # O(n)
        for i in range(0, n):
            l = left[i]
            r = right[i]
            p = l * r
            nums[i] = p

        return nums




        
