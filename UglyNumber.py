class Solution:
    def isUgly(self, n: int) -> bool:
        nn = [2, 3, 5]
        while n != 1 and n != 0:
            checked = True
            for num in nn:
                if n % num == 0:
                    n = n / num
                    checked = False
            if checked:
                break
                    
        return n == 1
        