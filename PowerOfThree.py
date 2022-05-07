class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: 
            return True
        if n < 3: 
            return False
        p = 1
        while p < n:
            p *= 3
        
        return p == n