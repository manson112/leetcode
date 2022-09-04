class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = max(0, len(s)-2)
        for i in range(len(s)-2):
            if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
                result -= 1
            
            
        return result