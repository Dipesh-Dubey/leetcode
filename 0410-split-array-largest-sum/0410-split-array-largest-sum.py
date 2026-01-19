class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l <= r:
            mid = (l + r) // 2
            subarr = 0
            mysum = 0

            for num in nums:
                if num + mysum <= mid:
                    mysum += num
                else:
                    subarr += 1
                    mysum = num
            subarr += 1

            if subarr > k:
                l = mid+1
            else:
                r = mid-1
        return l


                