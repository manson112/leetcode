class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return sum([1 if sum(c[:3]) == c[3] else 0 for c in itertools.combinations(nums, 4)])
