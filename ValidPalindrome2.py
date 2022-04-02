from calendar import c


class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                l = s[i:~i]
                r = s[i+1:len(s)-i]
                result = False
                if len(l) != 0:
                    result = result or l == l[::-1]
                if len(r) != 0:
                    result = result or r == r[::-1]
                return result
        return True
