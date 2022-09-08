class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        one = False
        seg = False
        for i in range(len(s)):
            if seg and s[i] == "1":
                return False
            elif s[i] == "1" and not one:
                one = True
            elif s[i] == "0" and one and not seg:
                one = False
                seg = True
        return True
                
            