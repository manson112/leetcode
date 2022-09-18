class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7:
            return n * (n+1) // 2
        m = (n-1) // 7
        
        k = 7 if n % 7 == 0 else n % 7
        l = m*k
        print(m, k, l)
        return m*28 + k*(k+1)//2 + (7 * (m-1)*m//2) + l

    
    