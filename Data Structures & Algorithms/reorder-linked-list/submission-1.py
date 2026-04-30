# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n, pos = 1, head

        while pos.next:
            pos = pos.next
            n += 1

        # iterate to half the 
        # if n == 1:
        #     return head

        left_read = n // 2 if n % 2 == 0 else n // 2 + 1 
        left_end_pos = head
        while left_read != 1: 
            left_end_pos = left_end_pos.next
            left_read -= 1

        pos = left_end_pos.next
        left_end_pos.next = None
        reverseHead = None
    
        while pos:
           oldPos = pos
           pos = pos.next 
           oldPos.next = reverseHead
           reverseHead = oldPos


        addPos = head
        while reverseHead: 
            nextPos = addPos.next 
            addPos.next = reverseHead
            reverseHead = reverseHead.next
            addPos.next.next = nextPos
            addPos = nextPos
            
            

