class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        l = 0
        for i, word in enumerate(words):
            l += len(word)
            if l > len(s):
                return False
            if l == len(s) and ''.join(words[:i+1]) == s:
                return True
        
        return False
                
                
        