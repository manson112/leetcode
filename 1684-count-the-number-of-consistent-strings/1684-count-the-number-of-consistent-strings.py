class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = Counter(allowed)
        for w in words:
            for i, c in enumerate(w):
                if allowed.get(c) == None:
                    break
                if i == len(w)-1:
                    count += 1
                    
        return count