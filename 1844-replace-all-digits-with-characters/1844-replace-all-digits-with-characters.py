class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        for i in range(1, len(s), 2):
            result += s[i-1] + chr(ord(s[i-1]) + int(s[i]))
        if len(s) % 2 == 1:
            result += s[-1]
        
        return result