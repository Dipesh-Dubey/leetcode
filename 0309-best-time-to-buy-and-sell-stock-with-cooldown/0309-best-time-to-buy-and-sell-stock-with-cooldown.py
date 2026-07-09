class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]

        def dfs_knap(i, flag):
            if i == n or i==n+1:
                return 0

            if dp[i][flag] != -1:
                return dp[i][flag]

            if not flag:
                dp[i][flag] = max(-prices[i] + dfs_knap(i+1, True),dfs_knap(i+1, False))
            else:
                dp[i][flag] = max(prices[i] + dfs_knap(i+2, False),dfs_knap(i+1, True))
            
            # print(dp)
            return dp[i][flag]

        return dfs_knap(0, False)