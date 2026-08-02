class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1] * n for _ in range(n)]
        def rec(i,j):
            if i==j: return piles[i]

            if dp[i][j] != -1: return dp[i][j]

            left = piles[i] - rec(i+1,j)
            right = piles[j] - rec(i,j-1)

            dp[i][j] = max(left,right)
            return dp[i][j]
            
        return rec(0,len(piles)-1) >= 0