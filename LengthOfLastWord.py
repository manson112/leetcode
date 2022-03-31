class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        firstSpace = True
        cnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and firstSpace:
                continue
            if s[i] == " ":
                break
            firstSpace = False
            cnt += 1
        return cnt
        # return len(s.strip().split(" ")[-1])