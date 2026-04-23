class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for num in nums:
                if num in perm: #to avoid duplicating values
                    continue
                perm.append(num)
                dfs(perm)
                perm.pop()
        
        dfs(perm)
        return res