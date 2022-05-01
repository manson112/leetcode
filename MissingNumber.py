class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = (len(nums) * (len(nums) + 1)) // 2
        for num in nums:
            s -= num
        return s