class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersections = nums[0]
        for i in range(1, len(nums)):
            intersection = set()
            for j in range(len(nums[i])):
                if nums[i][j] in intersections:
                    intersection.add(nums[i][j])
            intersections = list(intersection)
        return sorted(intersections)
            