from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
        

# basically for each character we are trying to 
# find the max window if we replace it it at most k 
# times

# slide a window across the string and count how many 
# characters inside it already match c. If the characters
# that don't match c is more than k, then the window is 
# invalid, so we have to shrink it by moving the left 
# pointer forwards. 
        




