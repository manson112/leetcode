class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = str(bin(start))[2:]
        goal = str(bin(goal))[2:]
        maxLen = max(len(start), len(goal))
        start = start.zfill(maxLen)
        goal = goal.zfill(maxLen)
        
        result = 0
        for i in range(len(start)):
            result += 1 if start[i] != goal[i] else 0
        return result
        