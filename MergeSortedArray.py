from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return
        
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == 0 and i >= m + j:
                nums1[i] = nums2[j] 
                j += 1
                continue
            if nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                del nums1[-1]
                j += 1
            i += 1
        print(nums1)
        