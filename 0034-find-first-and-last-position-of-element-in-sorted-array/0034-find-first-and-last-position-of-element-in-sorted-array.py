class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def f_index(nums,target):
            l = 0
            r = len(nums)-1
            track = -1

            while l<=r:
                mid = (l+r)//2

                if nums[mid]==target:
                    track = mid
                    r = mid-1
                elif nums[mid]>target:
                    r = mid -1 
                else:
                    l = mid + 1
            return track
        def l_index(nums,target):
            l = 0
            r = len(nums)-1
            track = -1

            while l<=r:
                mid = (l+r)//2

                if nums[mid]==target:
                    track = mid
                    l = mid+1
                elif nums[mid]>target:
                    r = mid -1 
                else:
                    l = mid + 1
            return track
        return [f_index(nums,target),l_index(nums,target)]
        
    