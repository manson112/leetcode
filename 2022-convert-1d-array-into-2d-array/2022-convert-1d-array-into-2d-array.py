class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        result = []
        for i in range(m):
            result += [original[i*n:i*n+n]]
        return result