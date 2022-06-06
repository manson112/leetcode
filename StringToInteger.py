class Solution:
    def myAtoi(self, s: str) -> int: 
        MAX = 2147483647
        MIN = -2147483648
        result = 0
        negative = False
        sign = False
        digitStarted = False
        for i in range(len(s)):
            if not digitStarted and s[i] == ' ':
                continue
            if not digitStarted and (s[i] == '+' or s[i] == '-'):
                if sign:
                    return 0
                negative = True if s[i] == '-' else False
                sign = True
                digitStarted = True
                continue
            num = ord(s[i]) - ord('0')
            isDigit = num >= 0 and num <= 9;  
            print(num, isDigit, result)
            if isDigit:
                digitStarted = True
                result = result*10 + num
            if not isDigit and digitStarted:
                break
            if result == 0 and not isDigit:
                break
            if result != 0 and not isDigit:
                break
        result = result * (-1 if negative else 1)
        result = MIN if result < MIN else result
        result = MAX if result > MAX else result
        
        return result
        
        
        
            
            
    
        