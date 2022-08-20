class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    result = max(result, nums[j] - nums[i])
        return result        