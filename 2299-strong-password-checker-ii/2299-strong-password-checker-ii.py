class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        spcList = list("!@#$%^&*()-+")
        if len(password) < 8:
            return False
        
        password = " " + password + " " 
        digit = False
        spc = False
        upper = False
        lower = False
        for i in range(1, len(password)-1):
            if password[i] == password[i-1] or password[i] == password[i+1]:
                return False
            if password[i] >= 'a' and password[i] <= 'z':
                lower = True
            if password[i] >= 'A' and password[i] <= 'Z':
                upper = True
            if password[i] >= '0' and password[i] <= '9':
                digit = True
            if password[i] in spcList:
                spc = True
        
        return digit and spc and upper and lower