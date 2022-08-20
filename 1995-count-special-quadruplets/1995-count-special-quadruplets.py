class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        counter = Counter(nums)
        coms = itertools.combinations(nums, 4)
        result = 0
        for c in coms:
            if sum(c[:3]) == c[3]:
                result += 1
        return result      
