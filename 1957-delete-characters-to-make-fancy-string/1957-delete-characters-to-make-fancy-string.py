class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        s += "!"
        
        prevIndex = 0
        prev = s[0]
        i = 1
        
        result = ""
        while i < len(s):
            if s[i] != prev:
                result += prev * (min(2, i-prevIndex))
                prev = s[i]
                prevIndex = i
            i += 1
            
        return result