class Solution:
    def getAnagramCode(self, s: str) -> str: 
        ana = [0] * 26 # one for each character
        base = ord('a')
        for ch in s: 
            # get the ORD index
            ana[ord(ch) - base] += 1
        return ana
            
    def isAnagram(self, s: str, t: str) -> bool:
        sCoded = self.getAnagramCode(s)
        tCoded = self.getAnagramCode(t)
        return sCoded == tCoded


        