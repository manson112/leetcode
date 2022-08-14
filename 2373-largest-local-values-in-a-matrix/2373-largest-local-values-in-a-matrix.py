class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def maxLocal(grid: List[List[int]], ii: int, jj: int) -> int:
            s = 0
            for i in range(ii, ii+3):
                for j in range(jj, jj+3):
                    s = max(s, grid[i][j])
            return s
        
        result = []
        for i in range(len(grid)-2):
            row = []
            for j in range(len(grid)-2):
                row += [maxLocal(grid, i, j)]
            result += [row]
        return result