class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxie,minie = -1,float("inf")
        minie_l = [0]*n
        
        for i in range(n-1,-1,-1):
            minie = min(minie,nums[i])
            minie_l[i] = minie
        
        # print(minie_l)
        
        for i in range(n):
            maxie = max(maxie,nums[i])
            # print(maxie - minie_l[i])
            if maxie - minie_l[i] <= k:
                return i
        
        return -1
        
