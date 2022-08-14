class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(list(str(num)))
        return int(num[0])*10 + int(num[3]) + int(num[1]) * 10 + int(num[2])