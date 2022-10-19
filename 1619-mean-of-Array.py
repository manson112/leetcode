class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        c = math.ceil(len(arr) / 20)
        return sum(arr[c:len(arr)-c]) / (len(arr)-2*c)
