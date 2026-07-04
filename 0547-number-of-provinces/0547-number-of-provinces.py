class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]* n

        def dfs(node):
            visited[node] = 1

            for nei in range(n):
                if isConnected[node][nei] == 1 and not visited[nei]:
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count+=1
        
        return count
                