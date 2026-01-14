class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        candidate = nums[0]

        for i in range(len(nums)):
            if nums[i] == candidate:
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                candidate = nums[i]
                counter = 1
       
        return candidate