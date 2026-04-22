class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r =  0, n - 1
        
        while l <= r:
            mid = abs((r + l) // 2)
            num = nums[mid]
            print(l, mid, r)

            if num == target:
                return mid
            elif num > target: 
                print(" - too big")
                r = mid - 1
            else:
                print(" - too small")
                l = mid + 1


        return -1 
