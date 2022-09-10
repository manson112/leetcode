class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = {}
        
        for i in range(lowLimit, highLimit+1):
            v = sum(map(int, list(str(i)))) 
            if c.get(v) == None:
                c[v] = 1
            else:
                c[v] += 1
        return max(c.values())