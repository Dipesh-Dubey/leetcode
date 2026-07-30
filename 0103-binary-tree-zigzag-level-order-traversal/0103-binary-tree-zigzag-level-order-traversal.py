# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque(([root]))
        res = []

        level = 0
        while q:
            level_l = []
            for i in range(len(q)):
                node = q.popleft()
        
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level_l.append(node.val)

            if level % 2 ==0: 
                res.append(level_l)
            else: 
                level_l.reverse()
                res.append(level_l)
            # print(res)

            level += 1
        return res
