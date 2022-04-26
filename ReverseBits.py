class Solution:
    def reverseBits(self, n: int) -> int:
        strBin = str(bin(n))[2:]
        return int(strBin[::-1] + ("0" * (32-len(strBin))), 2)
