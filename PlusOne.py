from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            s = carry + digits[i]
            digits[i] = s % 10
            carry = s // 10
        if carry != 0:
            digits = [carry] + digits
        return digits

print(Solution().plusOne([1,2,3]))