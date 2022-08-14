class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        nums = sorted(nums)
        l = 0
        r = 2
        result = 0
        i = 1
        print(nums)
        while i < len(nums)-1:
            while l > 0 and nums[l] == nums[i]:
                l -= 1
            while r < len(nums)-1 and nums[r] == nums[i]:
                r += 1
            print(l, r)
            if nums[l] < nums[i] and nums[i] < nums[r]:
                print(nums[l], nums[i], nums[r])
                result += (r - l - 1)
            l = r-1
            i = r
            r = i+1
        return result
            