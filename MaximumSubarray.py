from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -10000
        curSum = 0

        for i in range(len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)

        
        return maxSum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

