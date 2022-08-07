class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = 0
        brackets = [[0, 0]] + brackets
        for i in range(1, len(brackets)):
            if income <= brackets[i][0]:
                result += (income - brackets[i-1][0]) * (brackets[i][1] / 100)
                break
            else:
                result += (brackets[i][0] - brackets[i-1][0]) * (brackets[i][1] / 100)
        return result
                
                
            
                