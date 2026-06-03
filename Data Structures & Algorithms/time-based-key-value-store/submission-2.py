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
        prev_val = ""

        while l <= r:
            mid = (r - l) // 2 + l

            if values[mid][1] == timestamp:
                return values[mid][0]

            elif values[mid][1] < timestamp:
                l += 1
                prev_val = values[mid][0]

            else:
                r -= 1

        return prev_val

        
        
