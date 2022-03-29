class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = strs[0]
        for i in range(1, len(strs)):
            if len(strs[i]) < len(result):
                result = result[:len(strs[i])]
            for j in range(len(result)):
                if strs[i][j] != result[j]:
                    result = result[:j]
                    break
        return result


sol = Solution()
print(sol.longestCommonPrefix(["dog","racecar","car"]))