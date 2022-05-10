class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for ss in s:
            if dic.get(ss) == None:
                dic[ss] = 1
            else:
                dic[ss] += 1
        
        for tt in t:
            if dic.get(tt) == None:
                return tt
            else:
                dic[tt] -= 1
                if dic[tt] == 0:
                    del dic[tt]