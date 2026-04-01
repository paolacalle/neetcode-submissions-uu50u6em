class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        for i in range(n):
            l, r = i + 1, n - 1
            tmp_target_search = target - numbers[i]

            while l <= r: 
                mid = l + abs(r - l) // 2

                if numbers[mid] == tmp_target_search:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp_target_search:
                    l += 1
                else: 
                    r -= 1
        return []



        