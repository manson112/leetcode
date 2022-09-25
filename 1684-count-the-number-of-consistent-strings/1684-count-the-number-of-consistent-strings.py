class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = list(allowed)
        for w in words:
            isIn = True
            for c in w:
                if c not in allowed:
                    isIn = False
                    break
            
            count += 1 if isIn else 0
                    
        return count