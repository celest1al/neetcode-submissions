from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        check = [0] * 26
        window = [0] * 26
        a_charcode = ord('a')

        for ch in s1:
            check[ord(ch) - a_charcode] += 1
        
        for i, ch in enumerate(s2):
            window[ord(ch) - a_charcode] += 1

            if i >= m:
                window[ord(s2[i - m]) - a_charcode] -= 1
            
            if window == check:
                return True
        
        return False
        

        
