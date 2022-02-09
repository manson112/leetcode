class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        maxLength = 1
        for i in range(len(s)):
            for j in range(1+maxLength, len(s)-i+1):
                if self.findPelindrome(s[i:i+j]) and maxLength < j:
                    maxLength = j
                    result = s[i:i+j]
        return result

    def findPelindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False
        return True


s = Solution()
print(s.longestPalindrome("abcdbbfcba"))
