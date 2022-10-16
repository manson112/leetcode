class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        sortedList = sorted(c.items(), key=lambda x: (x[1], -x[0]))
        result = []
        for item in sortedList:
            for i in range(item[1]):
                result += [item[0]] 
        return result
