class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dic = {}
        for log in logs:
            for i in range(log[0], log[1]):
                if dic.get(i) == None:
                    dic[i] = 1
                else:
                    dic[i] += 1
        result = sorted(list(dic.items()), key=lambda x:(-x[1], x[0]))
        return result[0][0]