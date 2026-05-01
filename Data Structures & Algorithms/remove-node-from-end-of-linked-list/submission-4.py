# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linkedListLen = 0
        curr = head 
        while curr:
            linkedListLen += 1
            curr = curr.next

        prevIndex = linkedListLen - n
        pos = head

        if prevIndex == 0:
            return pos.next

        curr = head 
        while curr: 
            prevIndex -= 1
            
            if prevIndex == 0:
                tmp = curr.next 
                curr.next = curr.next.next
                tmp.next = None

                break 

            curr = curr.next

        

        return head



        


        
        