# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,targetSum):
            if not node:
                return False
            
            if not node.left and not node.right:
                if node.val==targetSum:
                    return True
            
            l = dfs(node.left,targetSum-node.val)
            r = dfs(node.right,targetSum-node.val)

            return l or r
        
        return dfs(root,targetSum)


