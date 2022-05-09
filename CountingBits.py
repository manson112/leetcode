class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]
        for i in range(1, n+1):
            arr += [sum(list(map(int, str(bin(i))[2:])))]
        return arr

        