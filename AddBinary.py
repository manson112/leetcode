class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        lenDiff = max(len(a), len(b)) - min(len(a), len(b))
        a = ("0" * lenDiff) + a if len(a) < len(b) else a
        b = ("0" * lenDiff) + b if len(b) < len(a) else b

        for i in range(len(a)-1, -1, -1):
            s = carry + int(a[i]) + int(b[i])
            result = str(s % 2) + result
            carry = s // 2
        
        if carry != 0:
            result = "1" + result

        return result

print(Solution().addBinary("11", "1"))