class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op in operations:
            if op[0] == '+' or op[-1] == '+':
                result += 1
            if op[0] == '-' or op[-1] == '-':
                result -= 1
        return result
                