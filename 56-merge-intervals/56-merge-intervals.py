class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=itemgetter(0))
        result = []
        for i, interval in enumerate(intervals):
            if i == 0:
                result += [interval] 
                continue
            if interval[0] <= result[-1][1] and interval[1] >= result[-1][1]:
                result[-1][1] = interval[1]
            elif interval[0] > result[-1][1]:
                result += [interval]
        return result