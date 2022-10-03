class Solution:
    def numberOfMatches(self, n: int) -> int:
        r = [1, 1, 2, 3, 4, 5, 6]

        result = 0
        t = n
        carry = 0
        while t > 1:
            print(t)
            if t < len(r):
                result += r[t-1]
                break
            if t % 2 == 0:
                result += t // 2
                t = t // 2 
            else:
                result += (t-1) // 2
                t = (t-1) // 2 + 1
            print(result)
            print()

        return result
