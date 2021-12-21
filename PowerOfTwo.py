class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bStr = bin(n)
        count = 0
        if n <= 0: return False
        for i in range(2, len(bStr)):
            if bStr[i] == "1":
                count += 1
            if count > 1:
                return False
        return True

