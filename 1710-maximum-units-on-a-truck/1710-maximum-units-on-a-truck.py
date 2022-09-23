class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1])
        maxUnits = 0
        for i in range(len(boxTypes)-1, -1, -1):
            m = min(boxTypes[i][0], truckSize)
            maxUnits += m*boxTypes[i][1]
            truckSize -= m
            if m <= 0:
                break
        return maxUnits
        