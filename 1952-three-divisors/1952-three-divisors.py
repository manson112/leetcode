class Solution:
    def isThree(self, n: int) -> bool:
        count = 2
        for i in range(n//2, 1, -1):
            if n % i == 0:
                count += 1
        return True if count == 3 else False