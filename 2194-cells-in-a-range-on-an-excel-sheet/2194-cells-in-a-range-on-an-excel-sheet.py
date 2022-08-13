class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        startDigit = s[1]
        endDigit = s[4]
        startChar = s[0]
        endChar = s[3]
        result = []
        for i in range(ord(startChar), ord(endChar)+1):
            for j in range(int(startDigit), int(endDigit)+1):
                result += [chr(i) + str(j)]
        return result
            