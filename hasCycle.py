# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        fast=head.next.next
        slow=head.next
        while(fast!=slow and fast and fast.next and fast.next.next):
            fast=fast.next.next
            slow=slow.next
        if slow!=fast:
            return False
        # elif slow==None:
        #     return False
        return True
        
