class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]* n

        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adj[i].append(j)
        
        def dfs(node):
            visited[node] = 1

            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count+=1
        
        return count
                