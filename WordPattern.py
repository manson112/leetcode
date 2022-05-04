class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        res = ""
        t = s.split(" ")
        if len(t) != len(pattern):
            return False
        for i in range(len(pattern)):
            if dic.get(pattern[i]) == None:
                if t[i] in dic.values():
                    return False
                dic[pattern[i]] = t[i]
                res += t[i] + " "
            else:
                res += dic[pattern[i]] + " "
        return res.strip() == s
    