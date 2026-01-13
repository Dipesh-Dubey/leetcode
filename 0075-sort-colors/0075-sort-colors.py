class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l , swaper = 0,0
        r = len(nums) - 1

        while swaper<=r:
            if nums[swaper] == 0:
                nums[l] , nums[swaper] = nums[swaper] , nums[l]
                l += 1
                swaper += 1
            elif nums[swaper] == 1:
                swaper += 1
                continue
            else:
                nums[swaper] , nums[r] = nums[r] , nums[swaper]
                r -= 1
        
        return nums
