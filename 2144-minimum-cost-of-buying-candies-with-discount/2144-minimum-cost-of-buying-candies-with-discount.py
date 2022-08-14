class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)
        
        cost = sorted(cost)
        result = 0
        for i in range(len(cost)-1, len(cost)%3 -1 , -3):
            result += cost[i] + cost[i-1]
        for i in range(len(cost) % 3):
            result += cost[i]
        return result