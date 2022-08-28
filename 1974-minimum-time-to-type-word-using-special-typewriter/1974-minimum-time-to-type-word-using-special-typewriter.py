class Solution:
    def minTimeToType(self, word: str) -> int:
        typingTime = len(word)
        
        cur = 'a'
        moveTime = 0
        for i in range(len(word)):
            moveTime += min(abs(ord(word[i]) - ord(cur)), 26 - abs(ord(word[i]) - ord(cur)))
            cur = word[i]
        return moveTime + typingTime
        
        