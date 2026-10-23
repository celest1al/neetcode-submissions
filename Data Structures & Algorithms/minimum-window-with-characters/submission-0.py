class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        if m < n:
            return ""

        if t == "":
            return ""
        
        check_counts = {}

        for i in range(n):
            check_counts[t[i]] = check_counts.get(t[i], 0) + 1
        
        window_counts = {}
        required = len(check_counts.keys())
        satisfied = 0
        left = 0
        best_start = -1
        best_length = m + 1

        for right in range(m):
            window_counts[s[right]] = window_counts.get(s[right], 0) + 1

            if s[right] in check_counts and window_counts[s[right]] == check_counts[s[right]]:
                satisfied += 1
            
            while satisfied == required:
                current_length = right - left + 1

                if current_length < best_length:
                    best_start = left
                    best_length = current_length
                
                if s[left] in check_counts:
                    if window_counts[s[left]] == check_counts[s[left]]:
                        satisfied -= 1
                    window_counts[s[left]] -= 1
                
                left += 1
        
        if best_start == -1:
            return ""
        else:
            return s[best_start:best_start + best_length]