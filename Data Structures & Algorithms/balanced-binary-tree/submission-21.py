# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # depths = keep track of the depths of each proccessed node
        # stack = dfs of the nodes
        # node is the current node we are trasvering 
        # last is the node we last proccessed
        depths = {}
        stack = []
        node = root
        last = None

        while stack or node:
            if node:
                # iterate all the way left first 
                stack.append(node)
                node = node.left
            else:
                # if no more left nodes, time to proccess the last updated node
                node = stack[-1]
                
                if not node.right or last == node.right:
                    # if node is a leaf or was the last node proccessed

                    # remove the last node from stack
                    # this node has now been fully proccessed
                    stack.pop() 

                    # get the depths of its left and right nodes
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    # verify it is balanced
                    if abs(left - right) > 1:
                        # subtree is unbalanced
                        return False 

                    # update the depth of the current proccessed note
                    # denote that this node was last seen
                    depths[node] = max(left, right) + 1
                    last = node 
                    node = None
                else:
                    node = node.right

        return True



        

        