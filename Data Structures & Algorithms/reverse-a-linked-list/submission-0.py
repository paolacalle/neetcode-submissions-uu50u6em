# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tempHead = None

        while head:
            oldHead = head
            head = head.next 
            oldHead.next = tempHead
            tempHead = oldHead

        head = None

        return tempHead
        

        