# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # not needed but good saftey 
        if not head and not head.next:
            return

        # determine length of the list : 0(n)
        n, pos = 1, head
        while pos.next:
            pos = pos.next
            n += 1

        # find the end of the left half : o(n)
        left_read = n // 2 if n % 2 == 0 else n // 2 + 1 
        left_end_pos = head

        while left_read != 1: 
            left_end_pos = left_end_pos.next
            left_read -= 1

        # reverse the right half  : O(N / 2)
        pos = left_end_pos.next
        left_end_pos.next = None
        reverseHead = None
    
        while pos:
           oldPos = pos
           pos = pos.next 
           oldPos.next = reverseHead
           reverseHead = oldPos

        # merge left and reversed right : O(n / 2)
        addPos = head
        while reverseHead: 
            # iterate
            nextLeft = addPos.next 
            nextRight = reverseHead.next 

            # update the pos with the reverse
            addPos.next = reverseHead
            reverseHead.next = nextLeft

            # update pointers to next points to check
            addPos = nextLeft
            reverseHead = nextRight
            
# time complexit: O(n) and space complexity : O(1)

