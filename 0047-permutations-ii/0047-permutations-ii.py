class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        perm = []
        used = [0]*len(nums)

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                if nums[i] in perm and used[i]:
                    continue
                used[i] = True
                perm.append(nums[i])
                dfs(perm)
                perm.pop()
                used[i] = False
        
        dfs(perm)
        return res