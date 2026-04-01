
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.cleanString(s)
        n = len(s)

        f, e = 0, n - 1

        while f != e and f < n and e > -1:
            if s[f] != s[e]:
                return False

            f += 1
            e -= 1 
        
        return True

    def cleanString(self, s: str) -> str: 
        s = s.lower()
        clean_chars = []
        for c in s: 
            if self.isAlphanumeric(c):
                clean_chars.append(c)
        return "".join(clean_chars)
        
    def isAlphanumeric(self, c: str) -> bool:
        return (
            ord('a') <= ord(c) <= ord('z') or 
            ord('A') <= ord(c) <= ord('Z') or 
            ord('0') <= ord(c) <= ord('9')
        )

        