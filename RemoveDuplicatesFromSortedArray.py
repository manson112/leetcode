from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 0
        while i < len(nums): 
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
                j += 1
        return j+1


sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))