class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        result = ""
        for word in words:
            pal = True
            for i in range(len(word)//2):
                if word[i] != word[len(word)-i-1]:
                    pal = False
                    break
            if pal:
                result = word
                break
        
        return result