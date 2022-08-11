class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        turn = []
        n = str(num)
        for i in range(len(n)):
            if int(n[i]) % 2 == 0:
                turn += [1]
                even += [int(n[i])]
            else:
                turn += [0]
                odd += [int(n[i])]
        
        odd = sorted(odd)
        even = sorted(even)
        result = ""
        
        for i in range(len(turn)):
            if turn[i] == 0:
                result += str(odd[-1]) 
                del odd[-1]
            else: 
                result += str(even[-1])
                del even[-1]
        return int(result)