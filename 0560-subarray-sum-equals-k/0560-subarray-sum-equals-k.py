class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = defaultdict(int)
        res = 0
        sum = 0
        ps[0] = 1

        for i in range(len(nums)):
            sum += nums[i]
            if sum-k not in ps:
                ps[sum] += 1
            else:
                res += ps[sum-k]
                ps[sum] += 1
        return res