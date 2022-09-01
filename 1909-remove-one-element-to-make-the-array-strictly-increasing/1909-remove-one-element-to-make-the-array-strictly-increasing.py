class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        nums = [-1] + nums + [2000]
        re = 0
        i = 2
        
        while i < len(nums)-1:
            if nums[i-1] >= nums[i]:
                print(i-1, i, "|", nums[i-1], nums[i])
                if nums[i-1] >= nums[i+1]:
                    nums = nums[:i-1] + nums[i:]
                    i -= 1
                else:
                    nums = nums[:i] + nums[i+1:]
                re += 1
            else :
                i += 1
            if re >= 2:
                return False
                    
        return True if re <= 1 else False
               
            
                
