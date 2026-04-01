from collections import defaultdict

# O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: count the number of times each
        # number shows up
        # mapped as --> numer : frequency count
        # o(n)
        size = len(nums)
        num_freq = defaultdict(int)
        freq = [[] for i in range(size + 1)] # 0, 1, 2, ... , n

        for n in nums:
            num_freq[n] += 1

        for num, cnt in num_freq.items():
            freq[cnt].append(num)

        res = []
        for i in range(size, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
        return res



        