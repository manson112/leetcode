class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0
        for i in range(len(str(num))-k+1):
            n = int(str(num)[i:i+k])
            if n != 0 and num % n == 0:
                result += 1
        return result