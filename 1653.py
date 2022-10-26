class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        if k == 0:
            return [0 for _ in range(len(code))]
        
        d = 1 if k > 0 else -1

        for i in range(len(code)):
            s = 0
            for j in range(i, i + abs(k)*d, d):
                s += code[(j+d) % len(code)]
            result += [s]
        return result
