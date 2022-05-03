class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        movedZero = 0
        while len(nums) - movedZero > i:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                movedZero += 1
            else:
                i += 1
            
