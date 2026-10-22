import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 1000000000
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if self.can_finish_eating(piles, h, mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
    
    def can_finish_eating(self, piles, h, k):
        total_hours = 0

        for pile in piles:
            total_hours += math.ceil(float(pile)/k)
        
        return total_hours <= h