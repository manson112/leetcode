class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        c = Counter(set(nums1))
        for n in set(nums2):
            c[n] += 1
        for n in set(nums3):
            c[n] += 1 
        result = []
        for k, v in c.items():
            if v >= 2:
                result += [k]
        return result
            