class Solution:
    def oneDigitMultiply(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            m = int(num1[i]) * int(num2) + carry
            carry = m // 10
            result = str(m % 10) + result
        if carry != 0:
            result = str(carry) + result
        return result

    def strPlus(self, num1: str, num2: str) -> str:
        maxLen = max(len(num1), len(num2))
        num1 = ("0"*(maxLen-len(num1))) + num1
        num2 = ("0"*(maxLen-len(num2))) + num2
        
        result = ""
        carry = 0
        for i in range(maxLen-1, -1, -1):
            p = int(num1[i]) + int(num2[i]) + carry
            carry = p // 10
            result = str(p % 10) + result
        if carry != 0:
            result = str(carry) + result
        return result
     
    def multiply(self, num1: str, num2: str) -> str:
        result = ""
        for i in range(len(num2)-1, -1, -1):
            oneDigitResult = self.oneDigitMultiply(num1, num2[i]) + ((len(num2)-1-i) * "0")
            result = self.strPlus(result, oneDigitResult)

        print(result)
        start = 0
        for i in range(len(result)):
            if result[i] != "0":
                start = i
                break
        if start == 0 and result[0] == "0":
            return "0"
        print(start)
        print(result[start:])
        return result[start:]    