class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pp = [1]*(len(nums)+1)
        sp = [1]*(len(nums)+1)
        res = [0] * len(nums)

        for i in range(len(nums)):
            pp[i+1] = pp[i] * nums[i]
            
        for i in range(len(nums)-1,-1,-1):
            sp[i-1] = sp[i] * nums[i]
        
        for i in range(len(nums)):
            res[i] = pp[i] * sp[i]
        
        return res