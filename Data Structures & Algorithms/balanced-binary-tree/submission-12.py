# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_height_balanced(self, root: Optional[TreeNode]):
        if not root or  (not root.left and not root.right):
            # root DNE or we at a leaf
            return 0

        # intialize the left and right heights
        left_height = right_height = 0

        if root.left:
            # recurvisly find the left-height
            left_height = self.dfs_height_balanced(root.left)

            # subtree was invaild
            if left_height == -1:
                return -1

            left_height += 1
            
        if root.right:
            right_height = self.dfs_height_balanced(root.right)

            # subtree was invaild
            if right_height == -1:
                return -1

            right_height += 1

        if abs(right_height - left_height) > 1:
            # mark subtree as invalid
            return -1 

        # return the depth we have encountered 
        return max(right_height, left_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # -1 is the flag for a violation within a subtree
        return self.dfs_height_balanced(root) != -1

        

        