from typing import List 

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        even = 0
        odd = 0
        for p in position:
            if p % 2 == 0: even += 1
            else: odd += 1        

        return min(even,odd)

            
             
print(Solution().minCostToMoveChips([2,2,2,3,3]))