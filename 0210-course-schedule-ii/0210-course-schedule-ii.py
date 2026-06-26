class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for crs,pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+=1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            for i in range(len(q)):
                node = q.popleft()

                for nei in adj[node]:
                    indegree[nei]-=1
                    if indegree[nei] == 0:
                        q.append(nei)
                res.append(node)

        if len(res) == numCourses: return res
        else: return []


        

        
        

