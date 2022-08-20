class Solution:
    def minimumMoves(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s)-3:
            if s[i] == 'X':
                result += 1
                i += 3
            else:
                i += 1
        for j in range(len(s)-1, i-1, -1):
            if s[j] == 'X':
                result += 1
                break
    
        return result
                