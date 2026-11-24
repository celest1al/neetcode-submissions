class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        candidates = sorted(nums)
        result, path = [], []

        def dfs(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                c = candidates[i]

                if c > remaining:
                    break
                
                path.append(c)
                dfs(i, remaining - c)
                path.pop()
        
        dfs(0, target)
        return result
