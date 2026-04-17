class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s, res = [], 0
        
        for v in operations: 
            a = None
            if v == "D":
                a = int(s[-1]) * 2
                s.append(a)
            elif v == "C":
                a = -1 * s.pop(-1)
            elif v == "+":
                a = int(s[-1]) + int(s[-2])
                s.append(a)
            else:
                a = int(v)
                s.append(a)

            res += a

        return res


        