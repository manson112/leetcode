class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

"""
limit = len(nums) / 2
dic = {}
for i in range(len(nums)):
    if dic.get(nums[i]) != None:
        dic[nums[i]] += 1
    else:
        dic[nums[i]] = 1
    if dic.get(nums[i]) >= limit:
        return nums[i]
"""