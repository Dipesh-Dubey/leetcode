class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
        if sum%2 != 0:
            return False

        sum = sum//2

        t = [[False]*(sum+1) for _ in range(n+1)]

        for i in range(n+1):
            t[i][0] = True
        
        for i in range(1,n+1):
            for j in range(1,sum+1):
                if nums[i-1]<=j:
                    t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]

                else:
                    t[i][j] = t[i-1][j]

        return t[n][sum]



