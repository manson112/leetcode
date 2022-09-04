class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxOnes = 0
        maxZeros = 0
        ones = 0
        zeros = 0
        
        for w in s:
            if w == '1':
                ones += 1
                maxOnes = max(maxOnes, ones)
                zeros = 0
            else:
                zeros += 1
                maxZeros = max(maxZeros, zeros)
                ones = 0
        
        return maxOnes > maxZeros