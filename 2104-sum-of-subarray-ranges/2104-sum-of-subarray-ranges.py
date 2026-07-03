class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        tot = 0
        for i in range(n):
            maxie = minie = nums[i]
            for j in range(i,n):
                maxie = max(maxie,nums[j])
                minie = min(minie,nums[j])
                tot += maxie - minie
     
        return tot