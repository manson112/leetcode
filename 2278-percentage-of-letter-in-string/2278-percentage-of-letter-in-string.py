class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = Counter(s)
        return int(c[letter]) * 100 // len(s)