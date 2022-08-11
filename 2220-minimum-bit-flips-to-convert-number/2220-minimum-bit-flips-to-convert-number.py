class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        print(bin(xor(start, goal))[2:])
        diff= bin(xor(start, goal))[2:]
        return sum(list(map(int, diff)))
            
            
        