class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        l = nums[0]
        r = sum(nums[2:])
        
        for i in range(1, len(nums)-1):
            if l == r:
                return i-1
            l += nums[i]
            r -= nums[i+1]
            
        return -1