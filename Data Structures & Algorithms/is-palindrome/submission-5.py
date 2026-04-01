class Solution:

    def isValid(self, ch: str) -> bool:
        o = ord(ch)
        if ord('a') <= o <= ord('z'):
            return True

        if ord('A') <= o <= ord('Z'):
            return True

        if ord('0') <= o <= ord('9'):
            return True

        return False
    

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, e = 0, n - 1

        while i < e:
            if not self.isValid(s[i]):
                i += 1
                continue

            if not self.isValid(s[e]):
                e -= 1
                continue

            if s[i].lower() != s[e].lower():
                return False

            i += 1 
            e -= 1

        return True


        