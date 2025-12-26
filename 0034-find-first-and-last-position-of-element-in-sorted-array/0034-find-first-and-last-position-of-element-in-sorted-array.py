class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def f_index(nums,target):
            l = 0
            r = len(nums)-1
            track = -1

            while l<=r:
                mid = (l+r)//2

                left = nums[mid-1] if mid-1>=0 else float('-inf')
                if left<nums[mid] and nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        def l_index(nums,target):
            l = 0
            r = len(nums)-1
            track = -1

            while l<=r:
                mid = (l+r)//2

                right = nums[mid+1] if mid+1<len(nums) else float('inf')
                if nums[mid]<right and nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r = mid -1 
                else:
                    l = mid + 1
            return -1
        return [f_index(nums,target),l_index(nums,target)]
        
    