class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for crs,pre in prerequisites:
            adj[pre].append(crs)
        
        visited = [False] * numCourses
        path = [False] * numCourses
        cycle = False

        def dfs(node):
            nonlocal cycle
            visited[node] = True
            path[node] = True

            for nei in adj[node]:
                if visited[nei] and path[nei]:
                    cycle = True
                    return

                elif not visited[nei]:
                    dfs(nei)
            
            path[node] = False
        
        for node in range(numCourses):
            if not visited[node]:
                dfs(node)
        
        if cycle==False: return True
        else: return False