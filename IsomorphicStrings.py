class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        res = ""
        for i in range(len(s)):
            if dic.get(s[i]) == None:
                if t[i] in dic.values():
                    return False
                dic[s[i]] = t[i]
                res += t[i]
            else:
                res += dic[s[i]]
        return res == t
                