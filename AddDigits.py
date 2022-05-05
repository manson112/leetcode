class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 != 0:
            s = 0
            for x in str(num):
                s += int(x)
            num = s
        return num