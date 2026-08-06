class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]

        for u,v in invocations:
            adj[u].append(v)

        visited = [0] * n

        def dfs(node):
            visited[node] = 1
            for nei in adj[node]:
                if visited[nei]==0:
                    dfs(nei)
        dfs(k)

        for u,v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))

        ans = []
        for i in range(n):
            if not visited[i]:
                ans.append(i)

        return ans