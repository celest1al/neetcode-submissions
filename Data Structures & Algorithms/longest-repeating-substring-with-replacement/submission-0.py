class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        longest = 0
        char_dict = {}
        left = 0
        max_freq = 0

        for right in range(len(s)):
            char_dict[s[right]] = char_dict.get(s[right], 0) + 1
            max_freq = max(max_freq, char_dict[s[right]])

            window_length = right - left + 1
            replacement = window_length - max_freq

            while replacement > k:
                char_dict[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                replacement = window_length - max_freq

            longest = max(longest, right - left + 1)
        
        return longest
