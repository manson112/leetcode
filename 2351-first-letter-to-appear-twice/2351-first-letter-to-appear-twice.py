class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = [0 for _ in range(26)]
        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                return s[i]
            count[ord(s[i]) - ord('a')] += 1
                    
            
                