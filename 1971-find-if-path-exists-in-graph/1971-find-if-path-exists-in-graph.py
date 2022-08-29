class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def findPath(d: dict, source:int, destination: int, visited: dict) -> bool:
            if destination == source:
                return True
            if visited.get(source) != None:
                return False
            visited[source] = True
            nodes = d[source]
            result = False
            for i in range(len(nodes)):
                result = result or findPath(d, nodes[i], destination, visited)
            return result
        
        
        dic = {}
        for edge in edges:
            if dic.get(edge[0]) == None:
                dic[edge[0]] = [edge[1]]
            else:
                dic[edge[0]] += [edge[1]]
            if dic.get(edge[1]) == None:
                dic[edge[1]] = [edge[0]]
            else:
                dic[edge[1]] += [edge[0]]
        
        visited = {}
        return findPath(dic, source, destination, visited)
        