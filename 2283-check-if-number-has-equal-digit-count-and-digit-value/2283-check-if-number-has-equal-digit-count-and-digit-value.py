class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i in range(len(num)):
            if num[i] != str(c[str(i)]):
                return False
        return True
        