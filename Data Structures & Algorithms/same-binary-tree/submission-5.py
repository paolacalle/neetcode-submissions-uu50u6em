# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True 

        if (not p and q) or (not q and p):
            return False

        if p and q and p.val != q.val: 
            return False

        if (
            (p.left and not q.left) or 
            (p.right and not q.right) or 
            (q.left and not p.left) or 
            (q.right and not p.right)
        ): return False 

        if p.left and q.left:
            return self.isSameTree(p.left, q.left)

        if p.right and q.right: 
            return self.isSameTree(p.right, q.right)

        return True 
        