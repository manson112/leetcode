class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        val = list(counter.values())[0]
        for k, v in counter.items():
            if v != val:
                return False
        return True
