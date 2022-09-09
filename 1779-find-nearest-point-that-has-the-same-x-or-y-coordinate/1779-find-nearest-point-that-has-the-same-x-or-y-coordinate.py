class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mhd = float('inf')
        result = -1
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                mh = abs(point[0]-x) + abs(point[1]-y)
                if mh < mhd:
                    mhd = mh
                    result = i
        return result
        
        