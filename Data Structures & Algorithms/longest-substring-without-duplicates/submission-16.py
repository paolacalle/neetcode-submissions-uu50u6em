class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        longest = 0
        i, j = 0, 1

        while j < n:
            print(s[j], s[i : j])
            if s[j] in s[i : j]:
                longest = max(
                    longest, 
                    (j - i)
                )

                while True:
                    if s[i] == s[j]:
                        break
                    i += 1
                i += 1
            j += 1 
        
        return max(longest, (j - i))

