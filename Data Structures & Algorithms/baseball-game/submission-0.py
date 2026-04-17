class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = [] # keep track of values
        
        for v in operations: 
            if v == "D":
                s.append(int(s[-1]) * 2)
            elif v == "C":
                s.pop(-1)
            elif v == "+":
                s.append(int(s[-1]) + int(s[-2]))
            else:
                s.append(int(v))
                
        return sum(s)


        