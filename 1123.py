class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        result = []
        for x in arr2:
            result += [x for _ in range(cnt[x])]
            del cnt[x]

        sorted_dict = {k: cnt[k] for k in sorted(cnt)}

        for x, y in sorted_dict.items():
            result += [x for _ in range(y)]

        return result
