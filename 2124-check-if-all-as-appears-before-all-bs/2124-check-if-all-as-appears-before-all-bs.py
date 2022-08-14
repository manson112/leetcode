class Solution:
    def checkString(self, s: str) -> bool:
        aApears = False
        for i in range(len(s)-1,-1,-1):
            if s[i] == 'a':
                aApears = True
            if aApears and s[i] == 'b':
                return False
        return True
    