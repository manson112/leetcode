class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxResult = -1
        result = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2] and int(num[i]) > maxResult:
                result = num[i]
                maxResult = int(num[i])
        return 3*result if result != "" else result