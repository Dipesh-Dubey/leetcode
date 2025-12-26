class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min,curr_max = 0,0
        global_min,global_max = nums[0],nums[0]
        total = sum(nums)

        for i in range(len(nums)):
            curr_min = min(curr_min+nums[i],nums[i])
            curr_max = max(curr_max+nums[i],nums[i])

            global_min = min(global_min,curr_min)
            global_max = max(global_max,curr_max)

        return max(total-global_min,global_max) if global_max>0 else global_max