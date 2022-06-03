
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sortedList = sorted(nums)
        s = 0
        for i in range(0, len(nums), 2):
            s += sortedList[i]    
        return s
