class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cS1 = Counter(s1)
        cS2 = Counter(s2)
        changes = []
        for k, v in cS1.items():
            if cS2.get(k) == None or cS2.get(k) != v:
                return False
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                changes += [i]
        if len(changes) == 0:
            return True
        if len(changes) != 2:
            return False
        
        return s1[changes[0]] == s2[changes[1]] and s1[changes[1]] == s2[changes[0]] 
        
        
            
        
