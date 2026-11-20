import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap: List[tuple[int, List[int]]] = []

        for point in points:
            heapq.heappush(min_heap, (point[0]**2 + point[1]**2, point))
        
        result = []

        for _ in range(k):
            current = heapq.heappop(min_heap)
            result.append(current[1])

        return result