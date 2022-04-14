from typing import List 

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)

        left = 0
        right = 0
        count = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                right += 1
                count += i
        
        for i in range(len(boxes)):
            result[i] = count
            if boxes[i] == "1":
                left += 1
                right -= 1
            
            count += left
            count -= right

        return result