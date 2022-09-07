class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word += 's'
        isDigit = False
        result = set()
        num = ""
        for i in range(len(word)):
            if ord(word[i]) in range(48, 58):
                isDigit = True
                num += word[i]
            else:
                if isDigit:
                    result.add(int(num))
                    num = ""
                isDigit = False
        return len(result)
                