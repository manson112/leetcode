class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = reduce(operator.mul, nums, 1)
        return 1 if res > 0 else 0 if res == 0 else -1
