class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> 
str:
        result = keysPressed[0]
        maxDuration = releaseTimes[0]

        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if diff > maxDuration:
                maxDuration = diff
                result = keysPressed[i]
            elif diff == maxDuration:
                result = max(result, keysPressed[i])
            
        return result
