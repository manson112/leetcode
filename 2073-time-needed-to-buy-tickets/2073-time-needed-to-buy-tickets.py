class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if tickets[k] == 1:
            return k+1
        result = 0
        for i in range(len(tickets)):
            if i < k:
                result += min(tickets[i], tickets[k])
            elif i > k:
                result += min(tickets[i], tickets[k]-1)
        return result + tickets[k]