# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: 
            return []

        queue = [(root, 1)]
        res = []

        while queue: 
            p, p_index = queue.pop(0)

            if len(res) < p_index:
                res.append([])
                
            res[p_index - 1].append(p.val)

            if p.left:
                queue.append((p.left, p_index + 1))

            if p.right: 
                queue.append((p.right, p_index + 1))

        return res 



        
