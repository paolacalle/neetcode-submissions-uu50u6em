class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # start at 0 b/c it is not part of the cycle 
        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # jump to the next node
            if slow == fast:
                # we found the intersection point
                break

        slow2 = 0
        while True:
            # jump one by one
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break 

        return slow 
        