class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        dp = [[-1]*m for _ in range(n)]

        def fn(i,j):
            if j==m: return 1
            if i ==n: return 0
              
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == t[j]:
                dp[i][j] = fn(i+1,j+1) + fn(i+1,j)
            else:
                dp[i][j] = fn(i+1,j)

            return dp[i][j]
        
        return fn(0,0)