class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, n = 0, len(s)
        i = 0

        for j in range(n):
            if s[j] in s[i : j]:
                while True:
                    if s[i] == s[j]:
                        break
                    i += 1
                i += 1

            longest = max(
                    longest, 
                    (j - i) + 1
            )
        
        return longest

