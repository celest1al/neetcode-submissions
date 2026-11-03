from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        for n, f in Counter(nums).items():
            buckets[f].append(n)
        
        result = []

        for c in range(len(buckets) - 1, 0, -1):
            for num in buckets[c]:
                result.append(num)

                if len(result) == k:
                    return result