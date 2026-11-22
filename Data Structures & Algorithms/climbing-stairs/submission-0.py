class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2

        def dfs(step):
            if step in memo:
                return memo[step]
            
            total_step = dfs(step - 1) + dfs(step - 2)
            memo[step] = total_step
            return memo[step]
        
        return dfs(n)