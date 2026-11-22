def is_valid_palindrome(s: str) -> bool:
    if len(s) == 1:
        return True
    
    lo, hi = 0, len(s) - 1

    while lo <= hi:
        if not s[lo].isalnum():
            lo += 1
        if not s[hi].isalnum():
            hi -= 1
        
        if s[lo].lower() != s[hi].lower():
            return False
        
        lo += 1
        hi -= 1
    
    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(idx, path):
            if idx == len(s):
                result.append(path[:])
                return
            
            for end in range(idx + 1, len(s) + 1):
                prefix = s[idx:end]
                if is_valid_palindrome(prefix):
                    path.append(prefix)
                    dfs(end, path)
                    path.pop()
        
        dfs(0, [])
        return result
