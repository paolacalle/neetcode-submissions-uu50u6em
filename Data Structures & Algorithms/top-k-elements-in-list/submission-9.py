from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for n in nums:
            num_freq[n] += 1

        print(num_freq)

        freq_num = defaultdict(set)
        for n, f in num_freq.items():
            freq_num[f].add(n)

        print(freq_num)


        res = []
        while k:
            av_keys = freq_num.keys()
            if not av_keys:
                print("left early")
                break 

            max_key = max(freq_num.keys())
            mk_items = freq_num[max_key]
            
            for i in mk_items:
                if k == 0:
                    break 

                res.append(i)
                k -= 1
                
            freq_num.pop(max_key)
            
        return res
        
        




        