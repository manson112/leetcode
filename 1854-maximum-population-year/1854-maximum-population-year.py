class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0 for i in range(101)]
        for log in logs:
            for i in range(log[0], log[1]):
                arr[i - 1950] += 1
                
        m = 0
        year = 0
        for i, v in enumerate(arr):
            if v > m:
                m = v
                year = i + 1950
        return year