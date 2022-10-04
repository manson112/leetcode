class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        cur = 0
        for ss in s:
            if ss == "(":
                cur += 1
                result = max(result, cur)
            if ss == ")":
                cur -= 1
        return result

