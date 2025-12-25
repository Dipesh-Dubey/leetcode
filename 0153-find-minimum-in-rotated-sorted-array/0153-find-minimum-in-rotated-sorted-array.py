class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1 
        Min = float('inf')

        if len(nums)==1:
            return nums[0]

        while l<=r:
            mid = (l+r)//2

            if nums[mid]>nums[r]:
                l = mid + 1
            
            else:
                Min = min(Min,nums[mid])
                r = mid - 1
        return Min
        
        