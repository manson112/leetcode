class Solution:
    def maxArea(self, height: List[int]) -> int:
        MAX = 0
        
        i = 0
        j = len(height)-1
        while i < j:
            MAX = max(MAX, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return MAX