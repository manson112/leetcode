# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        
        start = 1
        end = n
        index = 0
        lastSucIndex = 0
        lastBadIndex = 0
        while start <= end:
            r = isBadVersion((start + end) // 2)
            index = (start + end) // 2
            if r:
                lastBadIndex = index
                end = index - 1
            else:
                lastSucIndex = index
                start = index + 1
            
        if isBadVersion(index):
            start = index-1
            end = lastSucIndex-1
        else:
            start = lastBadIndex-1
            end = index-1

        for i in range(start, end, -1):
            if not isBadVersion(i):
                return i + 1