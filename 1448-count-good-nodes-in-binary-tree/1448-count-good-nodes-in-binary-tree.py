# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node,max_path):
            if not node:
                return 
            
            if node.val >= max_path:
                self.count += 1
                max_path = node.val
                
            l = dfs(node.left,max_path)
            r = dfs(node.right,max_path)
        
        dfs(root,root.val)
        return self.count



