class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        visited = [["T" for _ in range(n+2)]]
        for _ in range(m):
            visited += [["T"] + ["F" for _ in range(n)] + ["T"]]
        visited += [["T" for _ in range(n+2)]]
        t = 0
        next = [1, 1]
        result = []
        while t < m * n:
            print(next)
            visited[next[0]][next[1]] = "T"
            result += [matrix[next[0]-1][next[1]-1]]
            print("result:",result)
            print("next step:", next[0] + dr[d][0], ",", next[1] + dr[d][1])
            if visited[next[0] + dr[d][0]][next[1] + dr[d][1]] == "T":
                d = (d+1) % 4
            next = [next[0] + dr[d][0], next[1] + dr[d][1]]
            t += 1 
        return result