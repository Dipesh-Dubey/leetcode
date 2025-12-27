class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 1
        r = nums[0]
        max_index = 0
        jumps = 1
        
        while r<len(nums)-1:
            for i in range(l,r+1):
                max_index = max(max_index,nums[i]+i)        
            l = r+1
            r = max_index
            jumps += 1

        return jumps if len(nums)>1 else 0