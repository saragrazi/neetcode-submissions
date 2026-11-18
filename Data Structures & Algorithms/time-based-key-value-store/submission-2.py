class TimeMap:

    def __init__(self):
        self.mapi = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapi:
            self.mapi[key] = []
        self.mapi[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.mapi.get(key, [])
        res = ""
        left, right = 0, len(values) - 1
        while left <= right:
            med = (left + right) // 2
            if values[med][0] <= timestamp:
                res = values[med][1]   # מועמד טוב, ננסה למצוא מאוחר יותר
                left = med + 1
            else:
                right = med - 1
        return res