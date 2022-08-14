import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(0, len(nums)):
            heappush(heap, (-nums[i], [nums[i], i]))            
        return [x[0] for x in sorted([heappop(heap)[1] for _ in range(k)], key=lambda x: x[1])]