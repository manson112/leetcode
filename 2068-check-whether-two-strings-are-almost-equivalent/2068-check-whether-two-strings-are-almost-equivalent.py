class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for k, v in c1.items():
            r = v
            if c2.get(k) != None:
                r = abs(v-c2[k])
                del c2[k]
            if r >= 4:
                return False
        for k, v in c2.items():
            if v >= 4:
                return False
        return True
                
                
            