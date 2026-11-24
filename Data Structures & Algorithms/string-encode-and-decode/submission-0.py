class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        parts = []
        for s in strs:
            prefix = f"{len(s):4}"
            parts.append(prefix + s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        decoded_parts = []
        idx = 0
        n = len(s)

        while idx < n:
            str_length = int(s[idx:idx+4])
            idx += 4

            decoded = s[idx:idx+str_length]
            decoded_parts.append(decoded)
            idx += str_length
        
        return decoded_parts

        
