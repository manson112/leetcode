from itertools import permutations, product

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        MAX_HOUR = 3
        MAX_MIN = 5
        MAX_TURNON = MAX_HOUR + MAX_MIN
        
        if turnedOn > MAX_TURNON:
            return []
        ret = []
        for i in range(min(MAX_HOUR + 1, turnedOn + 1)):
            if turnedOn - i > MAX_MIN:
                continue
            tt = [self.getHour(i)] + [self.getMinute(turnedOn - i)]
            ttList = set(product(*tt))
            for item in ttList:
                s = sum(item)
                ret += [str(s // 60) + ":" + ("0" if len(str(s%60)) == 1 else "") + str(s % 60) ]
        return ret                
        
    
    def getHour(self, turnedOn: int) -> List[int]:
        ret = []
        items = [0 for _ in range(4 - turnedOn)] + [1 for _ in range(turnedOn)]
        perms = set(permutations(items, 4))
        for perm in perms:
            h = 60 * (perm[3] * 8 + perm[2] * 4 + perm[1] * 2 + perm[0])
            if h >= 720:
                continue
            ret += [h]
        return ret
    
    def getMinute(self, turnedOn: int) -> List[int]:
        ret = []
        items = [0 for _ in range(6 - turnedOn)] + [1 for _ in range(turnedOn)]
        perms = set(permutations(items, 6))
        for perm in perms:
            s = perm[5] * 32 + perm[4] * 16 + perm[3] * 8 + perm[2] * 4 + perm[1] * 2 + perm[0]
            if s >= 60:
                continue
            ret += [s]
        return ret

Solution().getHour(2)