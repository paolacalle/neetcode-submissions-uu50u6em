class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap_pos = 0
        n = len(nums)

        for i in range(n - 1, -1, -1):
            if nums[i] == val:
                nums[i] = nums[n - 1 - swap_pos]
                swap_pos += 1

        return n - swap_pos

        