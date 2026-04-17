class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs,
            key = lambda x : len(x)
        )

        s = strs[0]

        for i in range(len(s), 0, -1):
            
            match = True
            for w in strs:
                if not w[:i] == s[:i]:
                    match = False
                    break

            if match:
                return s[:i]

        return ""

        