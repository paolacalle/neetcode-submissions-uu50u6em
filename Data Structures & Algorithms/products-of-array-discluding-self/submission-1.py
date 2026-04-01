class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1] * n

        # populate the right
        # o(n)
        for i in range(1, n):
            product[i] = product[i - 1] * nums[i - 1]

        # populate the left
        # o(n)
        left = 1
        for i in range(n - 2, -1, -1):
            product[i] = left * nums[i + 1] * product[i]
            left *= nums[i + 1]

        return product




        
