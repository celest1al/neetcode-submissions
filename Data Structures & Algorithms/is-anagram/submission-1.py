from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for ch in s:
            counts[ch] += 1
        

        for ch in t:
            counts[ch] -= 1
        
        for _, val in counts.items():
            if val != 0:
                return False
            
        
        return True