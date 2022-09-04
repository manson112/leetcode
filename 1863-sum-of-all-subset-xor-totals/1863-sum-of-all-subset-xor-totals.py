class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = sum(nums)
        
        for i in range(2, len(nums)+1):
            for coms in itertools.combinations(nums, i):
                xor = coms[0]
                for j in range(1, i):
                    xor = xor ^ coms[j]
                result += xor
        return result
        