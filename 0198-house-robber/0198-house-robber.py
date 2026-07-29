class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*2 for _ in range(n)]

        def rec(i,flag):
            if i==n:
                return 0
            
            if dp[i][flag]!= -1:
                return dp[i][flag]

            if flag == False:
                dp[i][flag] = max(nums[i] + rec(i+1,True), rec(i+1,False))
            else:
                dp[i][flag] = rec(i+1,False)

            return dp[i][flag]
        
        return rec(0,False)