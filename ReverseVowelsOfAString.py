class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0 
        s = list(s)
        end = len(s) - 1 
        while start < end:
            if s[start] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                for j in range(end, start, -1):
                    if s[j] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                        s[start], s[j] = s[j], s[start]
                        end = j - 1
                        break
            start += 1
        return ''.join(s)