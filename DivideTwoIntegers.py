class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        mul = 1
        if dividend < 0:
            mul *= -1
        if divisor < 0:
            mul *= -1
        ret = mul * (abs(dividend) // abs(divisor))
        if ret > MAX_INT:
            return MAX_INT
        elif ret < MIN_INT:
            return MIN_INT
            
        return ret