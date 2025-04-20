# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while(head and head.val==val):
            head=head.next
        iter1=head
        while(iter1 and iter1.next):
            if iter1.next.val==val:
                next1=iter1.next.next
                while next1 and next1.val==val:
                    next1=next1.next
                iter1.next=next1
            iter1=iter1.next
        return head
        
