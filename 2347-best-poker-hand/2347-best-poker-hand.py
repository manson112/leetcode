class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        
        counts = [0 for _ in range(13)]
        for i in ranks:
            counts[i-1] += 1
        
        m = max(counts)
        if m >= 3:
            return "Three of a Kind"
        if m >= 2:
            return "Pair"
        return "High Card"
            