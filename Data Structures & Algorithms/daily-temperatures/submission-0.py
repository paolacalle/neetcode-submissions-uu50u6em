class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        s = [] # decreasing montonic and tuple : (temp, index_it_came_from)
        res = [0] * n

        for i, t in enumerate(temperatures):

            while s and i < n and t > s[-1][0]:
                temp, pos = s.pop()
                d = i - pos # distance
                res[pos] = d

            s.append((t, i))
        return res



        
        
        


