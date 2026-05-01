# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # calculate the len of the linked list
        linkedListLen = 0
        curr = head 
        while curr:
            linkedListLen += 1
            curr = curr.next

        # determine the index of the previous node
        prevIndex = linkedListLen - n
        pos = head

        # the previous node is the head
        if prevIndex == 0:
            return pos.next

        # iterate until we reach the previous node
        curr = head 
        while curr: 
            prevIndex -= 1
            
            if prevIndex == 0:
                # remove the desired node
                # and clean out the hanging pointer
                tmp = curr.next 
                curr.next = curr.next.next
                tmp.next = None
                break 

            curr = curr.next

        return head

# time compleixty : 0(n)
# space complexity : O(1)

        


        
        