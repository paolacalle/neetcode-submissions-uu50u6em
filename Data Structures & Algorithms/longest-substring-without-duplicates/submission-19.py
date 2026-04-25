class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, n = 0, len(s)
        i = 0

        seen = set()

        for j in range(n):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            longest = max(
                    longest, 
                    (j - i) + 1
            )
        
        return longest

