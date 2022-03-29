class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        strX = str(x)

        for i in range(len(strX)//2):
            if strX[i] != strX[len(strX)-i-1]:
                return False

        return True




sol = Solution()
print(sol.isPalindrome(121))        


