class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join([s[:-1] for s in sorted(s.split(" "), key=lambda x: (int(x[-1])))])