class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        result = 0
        for k, v in c.items():
            if v == 1:
                result += k
        return result