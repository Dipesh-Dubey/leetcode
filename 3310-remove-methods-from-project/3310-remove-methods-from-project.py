class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        dfs(k)

        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))

        ans = []
        for i in range(n):
            if not visited[i]:
                ans.append(i)

        return ans