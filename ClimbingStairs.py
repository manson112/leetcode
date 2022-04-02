import math
class Solution:
    def climbStairs(self, n: int) -> int:
        result = 1
        j = 1
        for i in range(n-1, n // 2 - 1, -1):
            if i < j :
                break
            result += math.comb(i, j)
            j += 1
        return result