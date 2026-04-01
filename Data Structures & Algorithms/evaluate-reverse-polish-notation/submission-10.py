class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digits = []

        for t in tokens: 
            if t == '+':
                digits.append(digits.pop() + digits.pop())
            elif t == '-':
                a, b = digits.pop(), digits.pop()
                digits.append(b - a)
            elif t == '*':
                digits.append(digits.pop() * digits.pop())
            elif t == '/':
                a, b = digits.pop(), digits.pop()
                digits.append(int(float(b) / a))
            else:
                digits.append(int(t))

        return digits[0]



