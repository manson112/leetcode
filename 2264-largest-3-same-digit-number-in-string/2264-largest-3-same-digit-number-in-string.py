class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxResult = -1
        result = ""
        for i in range(len(num)-2):
            if len(set(list(num[i:i+3]))) == 1 and int(num[i:i+3]) > maxResult:
                maxResult = int(num[i:i+3])
                result = num[i:i+3]
        return result