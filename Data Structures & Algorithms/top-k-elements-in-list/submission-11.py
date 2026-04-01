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
        for n, f in num_freq.items():
            freq_num[f].add(n)

        # step 3: iterate and get the top k numbers
        res = []
        while k:
            # get the max freq
            max_key = max(freq_num.keys())

            # get the the items associated with the mac
            mk_items = freq_num[max_key]
            
            # pull the number of items needed
            for i in mk_items:
                if k == 0:
                    break 

                res.append(i)
                k -= 1
                
            # if need another roation, rmv the key we already saw.
            freq_num.pop(max_key)
            
        return res
        




        