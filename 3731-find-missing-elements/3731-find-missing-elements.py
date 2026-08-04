class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minie = min(nums)
        maxie = max(nums)
        res = []
        # print(minie,maxie)

        for i in range(minie,maxie+1):
            if i not in nums: res.append(i)
        
        return res
