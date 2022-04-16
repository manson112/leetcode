class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        columnNumber -= 1
        
        while columnNumber > 25:
            result = chr(columnNumber % 26 + 65) + result
            columnNumber = columnNumber // 26 - 1
        result = chr(columnNumber + 65) + result
        return result