class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix)-1
        
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        i = mid
        if target < matrix[mid][0]:
            i = mid-1
            
        print(i)
        
        left = 0
        right = len(matrix[i])-1
        
        mid = (left + right) // 2
        if matrix[i][mid] == target:
            return True
        while left <= right :
            mid = (left + right) // 2
            if matrix[i][mid] == target:
                return True
            if matrix[i][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False