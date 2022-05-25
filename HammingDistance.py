class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        strX = f'{x:b}'
        strY = f'{y:b}'
        maxLen = max(len(strX), len(strY))
        strX =  "0" * (maxLen - len(strX))  +  strX
        strY =  "0" * (maxLen - len(strY))  +  strY
        
        ret = 0
        for i in range(maxLen):
            ret += 1 if strX[i] != strY[i] else 0
        return ret
