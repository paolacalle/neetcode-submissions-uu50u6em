# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_height_balanced(self, root: Optional[TreeNode]):
        if not root:
            # root DNE or we at a leaf
            return [True, 0]

        left = self.dfs_height_balanced(root.left)
        right = self.dfs_height_balanced(root.right)

        balanced = True if left[0] and right[0] and abs(right[1] - left[1]) < 2 else False
        return [balanced, max(right[1], left[1]) + 1]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # -1 is the flag for a violation within a subtree
        return self.dfs_height_balanced(root)[0]

        

        