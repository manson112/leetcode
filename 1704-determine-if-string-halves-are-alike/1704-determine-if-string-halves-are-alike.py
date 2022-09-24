class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s1 = Counter(s[:len(s)//2].lower())
        s2 = Counter(s[len(s)//2:].lower())
        
        count1, count2 = 0, 0
        
        for v in vowels:
            if s1.get(v) != None:
                count1 += s1[v]
            if s2.get(v) != None:
                count2 += s2[v]
        
        return count1 == count2