class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums = sorted(nums)
        left = 0
        right = len(nums)-1
        print(nums)
        minimum = pow(10, 5) + 1
        result = -1 * pow(10, 5) -1
        while left <= right:
            mid = (left + right) // 2
            m = nums[mid]
            print(m)
            if m < 0:
                left = mid + 1
            elif m > 0:
                right = mid - 1
            else:
                return 0
            if abs(m) < minimum:
                minimum = abs(m)
                result = m
            elif abs(m) == minimum:
                result = max(m, result)
        return result