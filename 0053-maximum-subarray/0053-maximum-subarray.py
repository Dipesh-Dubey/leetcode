class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float("-inf")
        maxie = float("-inf")

        for i in range(len(nums)):
            curr = max(nums[i],curr+nums[i])
            maxie = max(maxie,curr)
        
        return maxie