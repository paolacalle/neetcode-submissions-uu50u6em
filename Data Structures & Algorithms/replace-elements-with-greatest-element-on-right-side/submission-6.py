class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            curr_max, arr[i] = max(curr_max, arr[i] ), curr_max
        return arr
        