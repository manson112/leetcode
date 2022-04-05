from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary.keys:
                dictionary.pop(nums[i])
            else:
                dictionary[nums[i]] = True
        
        return dictionary.keys[0]