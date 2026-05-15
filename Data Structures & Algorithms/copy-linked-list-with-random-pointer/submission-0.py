"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        random_dict = {None: None} # current pointer -> random 

        if not head: return None


        # intialize
        curr = head
        while curr:
            random_dict[curr] = Node(curr.val, None, None)
            curr = curr.next

        # fill in 
        curr = head 
        while curr: 
            copy = random_dict[curr]
            copy.next = random_dict[curr.next]
            copy.random = random_dict[curr.random]
            curr = curr.next

        return random_dict[head]

        