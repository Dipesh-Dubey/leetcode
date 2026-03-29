class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #obtain subsets first
        total = sum(nums)

        if (target + total) % 2 != 0: #for odd sums
            return 0

        if abs(target) > total: #special edge case
            return 0

        s1 = (target+total)//2

        n = len(nums)
        t = [[0]*(s1+1) for _ in range(n+1)]

        for i in range(n+1):
            t[i][0] = 1
        
        for i in range(1,n+1):
            for j in range(0,s1+1): # include j = 0 for consistency
                if nums[i-1]<=j:
                    t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]

        return t[n][s1] 