class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = (10**9 + 7)
        for i in range(len(queries)):
            l,r,k,v = queries[i]
            while l<=r:
                nums[l] = (nums[l]*v) % MOD
                l += k
        
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor