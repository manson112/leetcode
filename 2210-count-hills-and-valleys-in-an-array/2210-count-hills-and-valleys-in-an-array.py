class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        n = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != n[-1]:
                n += [nums[i]]
                
        nums = n
        result = 0
        for i in range(1, len(nums)-1):
            if (nums[i-1] < nums[i] and nums[i+1] < nums[i]) or (nums[i-1] > nums[i] and nums[i+1] > nums[i]):
                result += 1
        return result