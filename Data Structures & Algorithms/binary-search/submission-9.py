class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # simple binary search algo
        n = len(nums)
        l, r =  0, n - 1
        
        # iterate until the ledt and right pointers overlap 
        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                # if the mid is the target, then
                # we found the number we are looking for
                return mid
            elif nums[mid] > target: 
                # if the number is too large, 
                # then our range is too high
                # update the right pointer
                r = mid - 1
            else:
                # if the number is too smal, 
                # then our range is too small
                # update the left pointer
                l = mid + 1
        # at this point, we have excuasted our search
        # meaning that we know that the list does not 
        # contain the target element
        return -1 
