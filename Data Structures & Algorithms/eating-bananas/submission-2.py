def feasible(piles, h, c):
    count = 0

    for pile in piles:
        count += (pile + c - 1) // c
    return count <= h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if feasible(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo