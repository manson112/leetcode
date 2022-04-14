class Solution:
    def isHappy(self, n: int) -> bool:
        dup = {}
        while True:
            s = 0
            while n > 0:
                num = n % 10
                s += num * num
                n = n // 10
            if s in dup:
                return False
            if s == 1:
                return True
            dup[s] = True
            n = s
            
        
print(Solution().isHappy(19))