class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = float("-inf")
        minimum = float("inf")
        
        for i in range(len(nums)):
            if minimum < nums[i]:
                result = max(result, nums[i]-minimum)
            minimum = min(nums[i], minimum)
            
        return result if result != float("-inf") else -1