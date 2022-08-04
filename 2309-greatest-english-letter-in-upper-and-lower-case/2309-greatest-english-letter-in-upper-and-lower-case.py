class Solution:
    def greatestLetter(self, s: str) -> str:
        alph = ['' for _ in range(26)]
        diff = ord('a') - ord('A')
        
        result = ""
        for i in range(len(s)):
            index = ord(s[i]) - (ord('a') if s[i] >= 'a' and s[i] <= 'z' else ord('A'))
            if alph[index] == '':
                alph[index] = s[i]
            elif alph[index] != s[i] :
                result = max(result.upper(), s[i].upper())
            
        return result