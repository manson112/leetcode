class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        maxLen = max(len(num1), len(num2))
        num1 = ("0" *  (maxLen - len(num1))) + num1
        num2 = ("0" *  (maxLen - len(num2))) + num2
        print(num1, num2)
        ret = ""
        carry = 0
        for i in range(maxLen-1, -1, -1):
            s = carry + int(num1[i]) + int(num2[i])
            carry = s // 10
            ret = str(s%10) + ret
        if carry != 0:
            ret = "1" + ret
        return ret