class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = start
        r = start

        while True:
            if nums[l] == target:
                return abs(l-start)
            if nums[r] == target:
                return abs(r-start)
            l = max(0, l-1)
            r = min(len(nums)-1, r+1)
        