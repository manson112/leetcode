class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        for i in range(1, len(s)//2 + 1):
            if len(s) % i == 0 and len(s.replace(s[:i], "")) == 0:
                return True
                
        return False
        
        
                