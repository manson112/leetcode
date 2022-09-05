class Solution:
    def sumBase(self, n: int, k: int) -> int:
        t = ""
        d = n
        while d != 0:
            t = str(d%k) + t
            d = d // k 
        
        return sum(map(int, t))
            