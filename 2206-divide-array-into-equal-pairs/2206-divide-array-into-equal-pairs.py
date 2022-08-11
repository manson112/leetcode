class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for e,c in c.items():
            if c % 2 != 0:
                return False
        return True
        