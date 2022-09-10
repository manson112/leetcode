class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = 0
        minWord = ""
        maxWord = ""
        
        if len(word1) < len(word2):
            minLen = len(word1)
            minWord = word1
            maxWord = word2
        else:
            minLen = len(word2)
            minWord = word2
            maxWord = word1
        
        result = ""
        for i in range(minLen):
            result += word1[i] + word2[i]
            
        result += maxWord[minLen:]
        return result