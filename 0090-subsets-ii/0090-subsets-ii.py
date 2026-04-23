class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        path = []

        def dfs(i,path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[i])
            if res[-1] != path:
                dfs(i+1,path)

            path.pop()
            if res[-1] != path:
                dfs(i+1,path)
        
        dfs(0,path)
        res.pop()
        return res