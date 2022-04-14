class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            s = 0
            while n > 0:
                num = n % 10
                s += num * num
                n = n // 10
            if s == 1:
                return True
            n = s
        