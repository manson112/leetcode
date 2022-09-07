class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result = set(edges[0])
        for i in range(1, len(edges)):
            result = result.intersection(set(edges[i]))
        
        return list(result)[0]