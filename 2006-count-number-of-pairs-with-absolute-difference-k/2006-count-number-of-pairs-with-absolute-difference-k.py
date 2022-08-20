class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        result = 0
        for num in nums:
            if num + k in c:
                result += c[num+k]
        return result