class TimeMap:

    def __init__(self):
        self.mapper = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapper:
            self.mapper[key] = []

        self.mapper[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.mapper.get(key, None)

        if not values:
            return ""

        l, r = 0, len(values) - 1
        prev_value = ""

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                prev_value = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return prev_value

        
        
