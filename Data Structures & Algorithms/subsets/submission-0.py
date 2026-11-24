class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        def dfs(start_idx):
            if start_idx == len(nums):
                result.append(path[:])
                return
            
            path.append(nums[start_idx])
            dfs(start_idx + 1)
            path.pop()
            dfs(start_idx + 1)
        dfs(0)
        return result