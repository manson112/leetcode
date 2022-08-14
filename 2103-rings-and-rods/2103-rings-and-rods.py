class Solution:
    def countPoints(self, rings: str) -> int:
        result = 0
        done = []
        rods = [set() for _ in range(10)]
        for i in range(1, len(rings), 2):
            rods[int(rings[i])].add(rings[i-1])
            if len(rods[int(rings[i])]) == 3 and int(rings[i]) not in done:
                done += [int(rings[i])]
                result += 1
        return result