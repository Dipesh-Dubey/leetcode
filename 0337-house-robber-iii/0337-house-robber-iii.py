# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0,0]
            
            l_node, l_skip = dfs(node.left)
            r_node, r_skip = dfs(node.right)

            n_node = node.val + l_skip + r_skip
            n_skip = max(l_node,l_skip) + max(r_node,r_skip)

            return [n_node,n_skip] 

        node_final, skip_final = dfs(root) 
        return max(node_final,skip_final)     