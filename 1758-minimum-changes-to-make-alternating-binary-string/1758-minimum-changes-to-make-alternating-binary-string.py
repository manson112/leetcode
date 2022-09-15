class Solution:
    def minOperations(self, s: str) -> int:
        res = [0] * 2
        for i, c in enumerate(s):
            res[i % 2 == int(c)] += 1
        return min(res)