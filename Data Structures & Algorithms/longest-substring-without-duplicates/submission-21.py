class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using a map solution 
        longest, n = 0, len(s)
        l = 0

        # keep track of the chracters last seen index
        # before being a dup
        mp = {} 

        for r in range(n):
            if s[r] in mp:
                # move the charater pos 
                # 1 more after its previous 
                # occurence 
                l = max(mp[s[r]] + 1, l)

            mp[s[r]] = r 
            longest = max(
                    longest, 
                    r - l + 1
            )

        return longest

