class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maxVal = nums[-1]
        if maxVal == 0:
            return maxVal
        if len(nums) == 1:
            return 1

        count = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] != cur:
                count += 1
                cur = nums[i]
        return count
