class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=r:
                r = i
        
        if r==0:
            return True
        return False

