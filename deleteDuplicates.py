# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter = head
        while(iter and iter.next):
            while iter and iter.next and iter.val==iter.next.val:
                iter.next=iter.next.next
            iter=iter.next
        return head
        
