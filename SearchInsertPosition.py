from typing import List


class Solution:
    def bSearch(self, nums: List[int], target: int, start: int, end: int, depth: int) -> int:
        if start == end or depth > len(nums):
            return start + (1 if nums[start] < target else 0)
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bSearch(nums, target, start, mid-1, depth + 1)
        else:
            return self.bSearch(nums, target, mid+1, end, depth + 1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bSearch(nums, target, 0, len(nums)-1, 1)

        
    
print(Solution().searchInsert([1,3], 0))