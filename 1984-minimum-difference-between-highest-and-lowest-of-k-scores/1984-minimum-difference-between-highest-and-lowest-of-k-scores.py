class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        res = sys.maxsize
        nums = sorted(nums)
        for i in range(len(nums)-k+1):
            n = nums[i:i+k]
            res = min(n[-1] - n[0], res)

        return res
            
            