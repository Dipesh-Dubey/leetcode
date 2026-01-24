class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            crt = nums[i]-1
            if nums[i] == nums[crt]:
                i +=1
            else:
                nums[i],nums[crt] = nums[crt],nums[i]

        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
                res.append(i+1)
        return res