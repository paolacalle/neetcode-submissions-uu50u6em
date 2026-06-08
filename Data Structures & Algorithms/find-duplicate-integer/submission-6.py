class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # start at 0 b/c it is not part of the cycle 
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]] # jump to the next node

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow 
        