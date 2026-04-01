from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: count the number of times each
        # number shows up
        # mapped as --> numer : frequency count
        num_freq = defaultdict(int)
        for n in nums:
            num_freq[n] += 1

        # step 2: inverse map 
        # map the frequency number to the numbers associated with it 
        # frequency --> set(num1, num2, ...)
        freq_num = defaultdict(set)
        max_f = 0
        for n, f in num_freq.items():
            freq_num[f].add(n)
            max_f = max(max_f, f)

        # step 3: iterate backward and get the top k numbers
        res = []
        for f in range(max_f, 0, -1):
            if f in freq_num:
                for n in freq_num[f]:
                    res.append(n)
                    if len(res) == k:
                        return res

        return res
        




        