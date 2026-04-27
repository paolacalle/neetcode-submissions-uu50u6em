class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            val = arr[i] 
            print(val, curr_max)
            arr[i] = curr_max
            curr_max = max(curr_max, val)

        return arr
        