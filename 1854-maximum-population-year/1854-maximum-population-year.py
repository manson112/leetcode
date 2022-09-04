class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        m = 0
        year = 0
        arr = [0 for i in range(101)]
        for log in logs:
            for i in range(log[0], log[1]):
                arr[i - 1950] += 1
                if arr[i-1950] > m:
                    year = i
                    m = arr[i-1950]
                elif arr[i-1950] == m:
                    if i < year:
                        year = i
                
                
        return year
