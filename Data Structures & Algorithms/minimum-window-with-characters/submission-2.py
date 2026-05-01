from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # count what we need : O(t)
        expectedMp = defaultdict(int)
        for i in t:
            expectedMp[i] += 1


        # store pos in s that matter : O(s)
        positionWithT = []
        for i in range(len(s)):
            if s[i] in expectedMp.keys():
                positionWithT.append(i)

        seenMp = defaultdict(int)

        required = len(expectedMp)
        formed = 0 

        l = 0 
        minLen = float("inf")
        minString = ""

        for r in range(len(positionWithT)):
            posR = positionWithT[r]
            charR = s[posR]

            seenMp[charR] += 1

            if seenMp[charR] == expectedMp[charR]:
                formed += 1


            while formed == required and l <= r: 
                posL = positionWithT[l]
                charL = s[posL]

                windowLen = posR - posL + 1

                if windowLen < minLen:
                    minLen = windowLen 
                    minString = s[posL : posR + 1]

                seenMp[charL] -= 1

                if seenMp[charL] < expectedMp[charL]:
                    formed -= 1

                l += 1

        return minString
        