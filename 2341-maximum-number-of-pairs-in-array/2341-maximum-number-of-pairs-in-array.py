class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 1]
        
        check = {}
        
        count = 0
        for i in range(len(nums)):
            if check.get(nums[i]) == None:
                check[nums[i]] = True
            else:
                del check[nums[i]]
                count += 1
        print(check)
        return [count, len(check.keys())]