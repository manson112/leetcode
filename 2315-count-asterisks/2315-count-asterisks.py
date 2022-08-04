class Solution:
    def countAsterisks(self, s: str) -> int:
        isIn = False
        count = 0
        for ss in s:
            if ss == '|':
                isIn = ~isIn
            if not isIn and ss == '*':
                count += 1
        return count