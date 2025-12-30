class Solution:
    def isSubtree(self, root, subRoot):
        def match(node,subRoot):
            if not node:
                return False
            if node.val == subRoot.val and compare(node,subRoot):
                return True
            l = match(node.left,subRoot)
            r = match(node.right,subRoot)

            return l or r
        
        def compare(node,subRoot):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False
            if node.val != subRoot.val:
                return False           
            return compare(node.left,subRoot.left) and compare(node.right,subRoot.right)
        
        return match(root, subRoot)
        
