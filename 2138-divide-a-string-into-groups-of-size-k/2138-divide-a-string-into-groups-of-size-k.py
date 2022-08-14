class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s)//k):
            result += [s[i*k:i*k+k]]
        if len(s) % k != 0:
            result += [s[len(s)//k*k:] + (k - len(s) % k) * fill]
        return result
        