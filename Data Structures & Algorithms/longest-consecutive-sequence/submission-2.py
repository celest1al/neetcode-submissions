class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in check:
                continue
            
            current_longest = 0
            current_num = num

            while current_num in check:
                current_longest += 1
                current_num += 1
            
            longest = max(longest, current_longest)
        
        return longest