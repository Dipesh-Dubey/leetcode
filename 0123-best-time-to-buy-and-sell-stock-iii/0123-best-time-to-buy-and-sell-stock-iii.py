class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n)] #imp

        def dfs_knap(i,flag,count):
            if i == n or count==0:
                return 0

            if dp[i][flag][count] != -1:
                return dp[i][flag][count]

            if not flag:
                dp[i][flag][count] = max(-prices[i] + dfs_knap(i+1,True,count),dfs_knap(i+1,False,count))
            else:
                dp[i][flag][count] = max(prices[i] + dfs_knap(i+1,False,count-1),dfs_knap(i+1,True,count))
                
            return dp[i][flag][count]

        return dfs_knap(0,False,2)