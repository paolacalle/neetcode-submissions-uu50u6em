class Solution:
    def checkIfDigit(self, token: str) -> bool:
        try:
            int(token)
        except ValueError as e:
            return False
        return True 

    def evalRPN(self, tokens: List[str]) -> int:
        digits = []

        for t in tokens: 
            if self.checkIfDigit(t):
                digits.append(t)
            else:
                if len(digits) > 1:
                    d1 = int(digits.pop())
                    d2 = int(digits.pop())

                    dr = None 

                    if t == "+":
                        dr = d2 + d1 
                    if t == "*":
                        dr = d2 * d1
                    if t == "-":
                        dr = d2 - d1
                    if t == "/":
                        if d1 == 0: 
                            return 101
                        dr = d2 / d1 

                    digits.append(dr)

        if not digits: 
            return -102

        print("h", digits)

        return int(digits.pop())



