class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        minR = 100
        for i in range(len(blocks)-k+1):
            numW = 1 if blocks[i] == 'W' else 0
            consB = 1 if blocks[i] == 'B' else 0
            convert = 1 if blocks[i] == 'W' else 0
            for j in range(i+1, i+k):
                if blocks[j] == 'W':
                    consB = 0
                    convert += 1
                else:
                    consB += 1
                if consB == k:
                    return 0
            minR = min(minR, convert)
            
        return minR
                
            
        
        
            
                
            