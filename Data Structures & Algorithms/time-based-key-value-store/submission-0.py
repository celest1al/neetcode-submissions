class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, value = "", self.store.get(key, [])

        lo, hi = 0, len(value) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if value[mid][1] <= timestamp:
                res = value[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res
