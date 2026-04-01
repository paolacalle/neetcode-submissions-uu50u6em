class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        n_set = len(set(nums))
        return not (n == n_set)
        