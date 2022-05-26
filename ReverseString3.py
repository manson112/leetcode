class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(" ")
        for i in range(len(ss)):
            ss[i] = ''.join(reversed(ss[i]))
        return " ".join(ss)