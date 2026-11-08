class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        result = hi

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p)/mid)
            
            if totalTime <= h:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
            
        return result