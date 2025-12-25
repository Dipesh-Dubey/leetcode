class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1 

        if len(nums)==1:
            return nums[0]

        while l<=r:
            mid = (l+r)//2
            left = nums[mid-1] if mid-1>=0 else float('inf')

            if nums[mid]>nums[r]:
                l = mid + 1
            
            else:
                if left>nums[mid]:
                    return nums[mid]
                r = mid - 1
        
        
        