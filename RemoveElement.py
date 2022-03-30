from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) <= 1:
            return 0 if len(nums) == 0  or nums[0] == val else 1

        i = 0
        j = len(nums) - 1
        while i <= j:
            while nums[j] == val and j >= 0:
                j -= 1
            if j == i:
                return i + 1
            elif j < i:
                return i
            
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


        
sol = Solution()
print(sol.removeElement([2,2,3], 2))