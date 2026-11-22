class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def dfs(idx, open_count, close_count):
            if idx == 2*n:
                result.append("".join(path))
                return
            
            if open_count < n:
                path.append("(")
                dfs(idx + 1, open_count + 1, close_count)
                path.pop()
            
            if close_count < open_count:
                path.append(")")
                dfs(idx + 1, open_count, close_count + 1)
                path.pop()
        
        dfs(0, 0, 0)
        return result