class Solution:
    def convert(self, ss: str, numRows: int) -> str:
        if numRows == 1:
            return ss
        ret = ["" for _ in range(numRows)]
        x = 0
        mode = 0
        for s in ss:
            ret[x] += s
            if x == numRows - 1:
                mode = 1
            elif x == 0:
                mode = 0
            
            x += 1 if mode == 0 else -1
        return ''.join(ret)