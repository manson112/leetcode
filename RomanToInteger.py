class Solution:
    
    def __init__(self) -> None:
        self.numDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "T": 0
        }

    def romanToInt(self, s: str) -> int:
        result = 0
        i = 1
        s = s + "T"
        while i < len(s):
            if self.getNum(s[i-1]) < self.getNum(s[i]):
                result += self.getNum(s[i]) - self.getNum(s[i-1])
                i += 2
            else:
                result += self.getNum(s[i-1])
                i += 1

        return result

    def getNum(self, s: str) -> int:
        return self.numDict[s]


sol = Solution()
print(sol.romanToInt("MCMXCIV"))