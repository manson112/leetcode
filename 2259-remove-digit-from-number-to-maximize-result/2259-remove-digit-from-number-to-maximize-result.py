class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        nums = []
        for i in range(len(number)):
            if number[i] == digit:
                nums += [number[:i] + number[i+1:]]
        return max(nums)