class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        maps = [0] * 10000

        for n in nums:
            if maps[n - 1] != 0:
                return n
                
            maps[n - 1] = 1
        