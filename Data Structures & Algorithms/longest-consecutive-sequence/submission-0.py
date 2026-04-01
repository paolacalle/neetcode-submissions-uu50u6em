from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_consecutive = {
            n : [] for n in nums
        }

        seen_n = set()
        for n in nums: 
            n_seq = n
            while True and (n not in seen_n):
                print(start_consecutive)
                n_seq += 1

                if n_seq in start_consecutive:
                    start_consecutive[n].append(n_seq)
                else:
                    break
            seen_n.add(n)

        max_size = 0
        for k, nums in start_consecutive.items():
            max_size = max(max_size, len(nums) + 1)

        return max_size




        