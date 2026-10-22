class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        window = [0] * 26
        a_charcode = ord("a")

        for i in range(len(s)):
            window[ord(s[i]) - a_charcode] += 1
        

        for j in range(len(t)):
            window[ord(t[j]) - a_charcode] -= 1
        
        for num in window:
            if num > 0:
                return False
        
        return True
