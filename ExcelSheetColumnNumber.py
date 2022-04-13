class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for s in columnTitle:
            result = result * 26 + ord(s) - 64
        return result