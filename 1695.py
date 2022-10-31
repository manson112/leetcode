class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")

        result = ""

        carry = ""
        limit = len(number)
        if len(number) % 3 == 1:
            limit = len(number) - 4
            carry = number[-4:-2] + "-" + number[-2:]

        i = 0
        while i < limit:
            result += number[i:min(i+3, limit)] + "-"
            i += 3
        
        if carry == "":
            result = result[:-1]
        else:    
            result += carry        
        return result
