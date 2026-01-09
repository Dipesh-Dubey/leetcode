class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps = defaultdict(int)
        ps[0] = 1
        sum = 0
        res = 0

        for i in range(len(nums)):
            sum += nums[i]
            modulo = sum % k
            if modulo not in ps:
                ps[modulo] += 1
            else:
                res += ps[modulo]
                ps[modulo] += 1
        
        return res