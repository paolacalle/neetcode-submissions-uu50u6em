# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head 

        steps = 1
        while fast and fast.next:
            steps += 1 
            fast = fast.next

            if steps % 3 == 0:
                slow = slow.next

            if slow == fast:
                return True

        return False

        