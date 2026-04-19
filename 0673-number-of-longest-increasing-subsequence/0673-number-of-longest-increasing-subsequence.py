class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp,count = [1]*n,[1]*n
        for ind in range(n):
            for prev_ind in range(ind):
                if nums[ind] > nums[prev_ind]:
                    if dp[prev_ind]+1 > dp[ind]:
                        dp[ind] = dp[prev_ind]+1
                        count[ind] = count[prev_ind]
                    elif dp[prev_ind]+1 == dp[ind]:
                        count[ind] += count[prev_ind]
        
        print(dp)
        print(count)

        maxi,index = 0,-1
        for i in range(n):
            if dp[i]>maxi: 
                maxi = dp[i]
                index = i
        
        counter = 0
        for i in range(n):
            if dp[i] == maxi:
                counter+=count[i]
                print(counter)

        return counter
        