class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = set(nums)
        best = 0

        for num in counts:
            if num - 1 not in counts:
                current = num
                current_count = 0

                while current in counts:
                    current += 1
                    current_count += 1
                
                best = max(best, current_count)
        
        return best