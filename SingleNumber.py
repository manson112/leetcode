class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for i in range(len(nums)):
            if dictionary.get(nums[i]) != None:
                dictionary.pop(nums[i])
            else:
                dictionary[nums[i]] = True
        for x in dictionary.keys():
            y = x
        return y