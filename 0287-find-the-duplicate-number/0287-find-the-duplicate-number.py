class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i<len(nums):
            crt = nums[i]-1
            if nums[i] == nums[crt]:
                i+=1
            else:
                nums[i],nums[crt] = nums[crt],nums[i]
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]
