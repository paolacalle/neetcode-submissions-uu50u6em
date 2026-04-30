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

        # use fast and slow pointer method
        # works b/c fast moves twice as fast
        # thus, by the time fast reaches the end, 
        # slow has only reached half of the distance
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # reverse the right half  : O(N / 2)
        pos = slow.next
        slow.next = None
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

