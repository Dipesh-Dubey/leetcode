class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        t = [[0]*c for _ in range(r)]
        t[0][0] = grid[0][0]

        for i in range(1,r):
            t[i][0] = t[i-1][0] + grid[i][0]
        # print(t)
        
        for i in range(1,c):
            t[0][i] = t[0][i-1] + grid[0][i]
        # print(t)

        for i in range(1,r):
            for j in range(1,c):
                t[i][j] = grid[i][j] + min(t[i-1][j],t[i][j-1])
        # print(t)
        
        return t[r-1][c-1]