class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        MOD = 12345
        pp = [[1]*n for _ in range(m)]
        sp = [[1]*n for _ in range(m)]
        res = [[1]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:   continue
                elif j==0:    pp[i][j] = (pp[i-1][n-1] * grid[i-1][n-1]) % MOD
                else:  pp[i][j] = (pp[i][j-1] * grid[i][j-1]) % MOD
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:   continue 
                elif j==n-1:    sp[i][j] = (sp[i+1][0] * grid[i+1][0]) % MOD
                else:   sp[i][j] = (sp[i][j+1] * grid[i][j+1]) % MOD
        
        for i in range(m):
            for j in range(n):
                res[i][j] = (pp[i][j] * sp[i][j]) % MOD
        
        return res

        




        