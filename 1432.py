class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        result = []
        for candy in candies:
            result += [True] if candy + extraCandies >= m else [False]
        return result
