from collections import defaultdict

class Solution:
    def getAnagramCode(self, s : str) -> str:
        anagramCode = [0] * 26 
        base = ord('a')

        for ch in s: 
            i = ord(ch) - base
            anagramCode[i] += 1

        return anagramCode

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped = defaultdict(list[str])

        for s in strs: 
            s_code = str(self.getAnagramCode(s))
            grouped[s_code].append(s)
            
        return list(grouped.values())


        