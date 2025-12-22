class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = l + (r-l)//2

            if nums[mid]==target:
                return True
            elif nums[mid]>nums[r]:
                if nums[l]<=target and target<nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1 
            elif nums[mid]<nums[r]:
                if nums[mid]<target and target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                r -= 1
        return False