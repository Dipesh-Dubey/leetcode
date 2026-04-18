class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp, parent = [1]*n, [-1]*n
        for ind in range(n):
            for prev_ind in range(ind):
                if nums[ind] % nums[prev_ind] ==0:
                    if dp[prev_ind]+1 > dp[ind]:
                        dp[ind] = dp[prev_ind]+1
                        parent[ind] = prev_ind
        
        maxi,index = 0,0
        for i in range(n):
            if dp[i]>maxi: 
                maxi = dp[i]
                index = i
        ans = []
        while index!=-1:
            ans.append(nums[index])
            index = parent[index]
        return ans