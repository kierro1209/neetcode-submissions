from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        seen = set()
        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(node):
            if node in seen:
                return False
            if graph[node] == []:
                return True
            
            seen.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            seen.remove(node)
            graph[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True