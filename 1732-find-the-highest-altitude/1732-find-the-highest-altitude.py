class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for g in gain:
            alt += [g+alt[-1]]
        return max(alt)