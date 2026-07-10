class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colour = [-1]*n
        self.res = True

        def dfs(node,c):
            colour[node] = c

            for nei in graph[node]:
                if colour[nei] != -1 and colour[nei] == c:
                    self.res = False

                if colour[nei] == -1:
                    if c==0: dfs(nei,1)
                    else: dfs(nei,0)
            
        for i in range(n):
            if colour[i] == -1:
                dfs(i,0)

        return self.res