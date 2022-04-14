from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        colMax = [0] * len(grid)
        rowMax = [max(grid[i]) for i in range(len(grid)) ]

        for i in range(len(grid)):
            cM = 0
            for j in range(len(grid)):
                cM = max(grid[j][i], cM)
            colMax[i] = cM

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == colMax[j] or grid[i][j] == rowMax[i]:
                    continue
                result += min(colMax[j], rowMax[i]) - grid[i][j]
                    
        return result


print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))