# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_length(self, root: Optional[TreeNode], height: int = 0):
        if not root or  (not root.left and not root.right):
            # we are at a leaf 
            return 0

        if height == -1:
            return -1

        # intialize the left and right heights
        left_height = right_height = height

        if root.left:
            # recurvisly find the left-height
            left_height = self.dfs_length(root.left, height)

            # subtree was invaild
            if left_height == -1:
                return -1

            left_height += 1
            
        if root.right:
            right_height = self.dfs_length(root.right, height)

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
        # simple edge cases
        # if (not root) or (not root.left and not root.right): 
        #     return True

        return self.dfs_length(root) != -1

        

        