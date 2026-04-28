# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        endPos = None 
        
        while list1 and list2:
            swap = None
            if list1.val <= list2.val:
                swap = list1
                list1 = swap.next
            else:
                swap = list2
                list2 = swap.next

            if endPos:
                endPos.next = swap
                swap.next = None 
                endPos = swap
            else:
                merged = swap
                endPos = swap
                swap.next = None

        if list1 and merged:
            endPos.next = list1
            return merged
        
        if list2 and merged:
            endPos.next = list2
            return merged

        return list1 if list1 else list2

