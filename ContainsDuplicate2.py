class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if dic.get(nums[i]) == None:
                dic[nums[i]] = i
                continue
            if abs(dic[nums[i]] - i) <= k:
                return True
            dic[nums[i]] = i
        return False