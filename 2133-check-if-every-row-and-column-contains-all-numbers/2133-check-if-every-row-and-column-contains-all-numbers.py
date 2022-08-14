class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        col =[[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            row = [0 for _ in range(len(matrix))]
            for j in range(len(matrix)):
                row[matrix[i][j]-1] = 1
                col[j][matrix[i][j]-1] = 1
            if sum(row) != len(matrix):
                return False
        for i in range(len(col)):
            if sum(col[i]) != len(matrix):
                return False
        return True
            
            