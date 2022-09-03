class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def equal(source, target):
            for i, s in enumerate(source):
                if s != target[i]:
                    return False
            return True
    
        def rotate(arr):
            nArr = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if arr[i][j] == 1:
                        nArr[j][len(arr)-1-i] = 1
            return nArr
        
        tmp = mat
        for i in range(4):
            tmp = rotate(tmp)
            print(tmp)
            if equal(tmp, target):
                return True
        return False