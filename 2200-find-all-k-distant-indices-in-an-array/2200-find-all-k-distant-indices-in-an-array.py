class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        s = set()
        for i in range(len(nums)):
            if nums[i] == key:
                start = 0 if i-k < 0 else i-k
                end = (len(nums) - 1) if i+k >= len(nums) else i+k
                for j in range(start, end+1):
                    s.add(j)
        
        return sorted(list(s))