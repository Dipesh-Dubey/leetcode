class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 
                    count += dp[r+1][c+1]

                
        return count