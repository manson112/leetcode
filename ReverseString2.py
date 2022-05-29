class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ret = ""
        for i in range(0, len(s), 2*k):
            ret += ''.join(reversed(s[i:i+k])) + s[i+k:i+2*k]
        return ret