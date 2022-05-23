class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        m = [nums[0], -2147483649, -2147483649]
        for i in range(1, len(nums)):
            if m[0] < nums[i]:
                m = [nums[i]] + m[:2]
            elif m[2] < nums[i]:
                if m[1] < nums[i]:
                    m = [m[0]] + [nums[i]] + [m[1]]
                else:
                    m = m[:2] + [nums[i]]
            print(m)
        if m[2] == -2147483649:
            return m[0]
        else :
            return m[2]
        
                
            
                
