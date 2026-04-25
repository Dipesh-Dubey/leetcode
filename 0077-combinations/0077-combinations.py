class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        nums = []
        for i in range(1,n+1):
            nums.append(i)

        def dfs(i,path):
            if len(path)==k:
                res.append(path.copy())
                return
            if i==len(nums):
                return
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
            dfs(i+1,path)
            
        dfs(0,path)
        return res