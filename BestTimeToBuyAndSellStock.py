from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        
        profit = 0
        for i in range(1, len(prices)):
            if minimum > prices[i]:
                minimum = prices[i]
                continue
            profit = max(profit, prices[i]-minimum)
        
        return profit


print(Solution().maxProfit([7,6,4,3,1]))