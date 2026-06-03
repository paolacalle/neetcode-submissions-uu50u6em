from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.mapper = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapper[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.mapper[key]

        if not values:
            return ""

        l, r = 0, len(values) - 1

        while l < r:
            mid = l + (r - l + 1) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                l += 1
            else:
                r -= 1

        if values and values[l][1] <= timestamp:
            return values[l][0]

        return ""

        
        
