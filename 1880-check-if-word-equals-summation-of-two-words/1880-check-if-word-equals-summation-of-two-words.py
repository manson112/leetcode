class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def toNum(word):
            n = 0
            for w in word:
                n = n * 10 + (ord(w) - ord('a'))
            return n
        
        return toNum(targetWord) == toNum(firstWord) + toNum(secondWord)            