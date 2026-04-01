class Solution:

    def isValid(self, ch: str) -> bool:
        o = ord(ch)
        if (o >= 65 and o <= 89):
            return True

        if (o >= 97 and o <= 122):
            return True

        if (o >= 48 and o <= 57):
            return True

        return False
    

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, e = 0, n - 1

        while i < e:
            if i >= n or e < 0:
                print("out of bound")
                return False

            if not self.isValid(s[i]):
                print(s[i], f" at {i} is not a letter")
                i += 1
                continue

            if not self.isValid(s[e]):
                print(s[e], f" at {e} not a letter")
                e -= 1
                continue

            if s[i].lower() != s[e].lower():
                print(f"{s[i]} != {s[e]}")
                return False

            i += 1 
            e -= 1

        print(e, i)

        return True


        