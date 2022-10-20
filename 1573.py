class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        
        result = 0
        i = 0
        j = len(mat)-1
        while i < len(mat):
            result += mat[i][i] + mat[i][j]
            i += 1
            j -= 1
        
        result -= 0 if len(mat) % 2 == 0 else mat[len(mat)//2][len(mat)//2]                    
        return result
