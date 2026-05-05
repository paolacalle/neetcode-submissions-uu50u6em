# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        merged = None
        merged_add_pos = None

        while True:
            smallest_val = float("inf")
            smallest_ls_pos = None 

            all_empty = 0 
            for l in lists:
                if not l:
                    all_empty += 1

            if all_empty == len(lists):
                break

            for idx, l in enumerate(lists):
                if l and l.val < smallest_val:
                    smallest_val = l.val
                    smallest_ls_pos = idx

            if merged: 
                merged_add_pos.next = lists[smallest_ls_pos]
                merged_add_pos = merged_add_pos.next
            else:
                merged = lists[smallest_ls_pos]
                merged_add_pos = merged 

            lists[smallest_ls_pos] = lists[smallest_ls_pos].next
            merged_add_pos.next = None

        return merged
