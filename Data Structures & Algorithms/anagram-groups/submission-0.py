from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            window = [0] * 26

            for ch in str:
                window[ord(ch) - 97] += 1
            
            key = tuple(window)
            groups[key].append(str)
        
        return list(groups.values())