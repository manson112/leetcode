class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(list(map(int, str(bin(n))[2:])))

            
