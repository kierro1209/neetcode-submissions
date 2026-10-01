# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def sameTree(a,b):
            if a == None and b == None:
                return True
            if not b or not a or a.val != b.val:
                return False
            
            return sameTree(a.right, b.right) and sameTree(a.left, b.left)
        
        if sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)