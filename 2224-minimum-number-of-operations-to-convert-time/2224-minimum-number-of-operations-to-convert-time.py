class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = 60 * int(current.split(":")[0]) + int(current.split(":")[1])
        correct = 60 * int(correct.split(":")[0]) + int(correct.split(":")[1])
        diff = correct - current
        
        time = [60, 15, 5, 1]
        
        result = 0
        for t in time:
            result += diff // t
            diff = diff % t
        return result
        
        