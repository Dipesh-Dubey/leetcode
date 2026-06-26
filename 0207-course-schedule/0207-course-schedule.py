class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for crs,pre in prerequisites:
            adj[pre].append(crs)
        
        visited = [False] * numCourses
        path = [False] * numCourses
        self.cycle = False

        def dfs(node):
            visited[node] = True
            path[node] = True

            for nei in adj[node]:
                if visited[nei] and path[nei]:
                    self.cycle = True
                    return

                elif not visited[nei]:
                    dfs(nei)
            
            path[node] = False
        
        for node in range(numCourses):
            if not visited[node]:
                dfs(node)
        
        if self.cycle==False: return True
        else: return False