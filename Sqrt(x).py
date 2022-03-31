class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 2
        right = x // 2
        while (left <= right) :
            mid = (left + right) // 2
            sqrt = mid * mid
            if sqrt < x:
                left = mid + 1
            elif sqrt > x:
                right = mid - 1
            else:
                return mid
        return left - 1