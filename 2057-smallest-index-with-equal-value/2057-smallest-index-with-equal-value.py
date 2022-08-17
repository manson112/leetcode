class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        result = -1
        for i, num in enumerate(nums):
            if i % 10 == num:
                result = i
                break
        return result