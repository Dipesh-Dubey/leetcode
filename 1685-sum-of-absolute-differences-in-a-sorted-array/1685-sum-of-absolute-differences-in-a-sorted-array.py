class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ps = [0] * (len(nums)+1)
        ss = [0] * (len(nums)+1) 
        res = []

        for i in range(len(nums)):
            ps[i+1] = ps[i] + nums[i]
            ss[i+1] = ss[i] + nums[len(nums)-1-i]

        for i in range(len(nums)):
            res.append( -ps[i] + ss[len(nums)-1-i] + nums[i]*((2*i)-len(nums)+1))
        
        return res