class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        nums += [nums[-1]+2]
        result = []
        start = 0
        end = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if start == end:
                    result += [str(nums[start])]
                else:
                    result += [str(nums[start]) + "->" + str(nums[end])]
                start = i
                end = i
            else:
                end = i
        return result