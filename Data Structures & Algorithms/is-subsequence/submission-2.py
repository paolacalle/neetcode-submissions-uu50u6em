class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n_s = len(s)

        for r in range(len(t)):
            if not (i < n_s):
                return True 

            if t[r] == s[i]:
                i += 1


        return not (i < n_s)
        