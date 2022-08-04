class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            diagonal = set([(i, i), (i, len(grid[i])-1-i)])
            for j in range(len(grid[i])):
                if grid[i][j] != 0 and (i, j) not in diagonal:
                    return False
                if grid[i][j] == 0 and (i, j) in diagonal:
                    return False
        
        return True