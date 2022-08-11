class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        counters = [Counter("")]
        for word in words:
            cw = Counter(word)
            if counters[-1] == cw:
                continue
            result += [word]
            counters += [cw]
        return result