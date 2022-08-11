class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = ""
            for i in range(0, len(s)//k + (1 if len(s) % k != 0 else 0)):
                print(i*k)
                d = s[i*k:i*k+k]
                print(d)
                tmp += str(sum(list(map(int, d))))
            s = tmp
        return s