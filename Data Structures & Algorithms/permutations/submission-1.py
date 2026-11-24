class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        n = len(nums)
        used = [False] * n

        def dfs():
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False
        
        dfs()
        return result