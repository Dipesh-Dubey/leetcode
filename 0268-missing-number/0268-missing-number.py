class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums): 
            if nums[i] == i or nums[i] == len(nums):
                i +=1  
            else:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        if len(nums) not in nums:
            return len(nums)