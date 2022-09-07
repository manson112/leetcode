class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) < 2:
            return True
        c = []
        for word in words:
            c.extend(word)
        print(c)
        c = Counter(c)
        for k, v in c.items():
            if v % len(words) != 0:
                return False
        return True
                