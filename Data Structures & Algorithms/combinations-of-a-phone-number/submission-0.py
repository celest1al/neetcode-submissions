KEYBOARD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        result = []
        def dfs(idx, path):
            if idx == len(digits):
                result.append("".join(path))
                return
            
            digit = digits[idx]

            for ch in KEYBOARD[digit]:
                path.append(ch)
                dfs(idx + 1, path)
                path.pop()
        
        dfs(0, [])

        return result