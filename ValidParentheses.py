class Solution:
    def isValid(self, s: str) -> bool:
        opens = {"[":0, "{":1, "(":2}
        closes = {"]":0, "}":1, ")":2}

        stack = []

        for x in s:
            if x in opens:
                stack += [x]
            else:
                if len(stack) == 0 : 
                    return False
                if opens[stack[-1]] == closes[x]:
                    stack = stack[:-1]
                else:
                    return False

        if len(stack) != 0:
            return False

        return True


sol = Solution()
print(sol.isValid("(("))