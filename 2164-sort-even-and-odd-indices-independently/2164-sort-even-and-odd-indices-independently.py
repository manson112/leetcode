class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums
    
        even = sorted([nums[i] for i in range(0, len(nums), 2)])
        odd  = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)        
        e = 0
        o = 0
        result = []
        for i in range(len(nums)):
            if i % 2 == 0:
                result += [even[e]]
                e += 1
            else:
                result += [odd[o]]
                o += 1
        return result