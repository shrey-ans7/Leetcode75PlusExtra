# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        res=-sys.maxsize
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=head
        while(curr.next!=slow):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        curr.next=prev
        while(slow and curr):
            res=max(res,slow.val+curr.val)
            slow=slow.next
            curr=curr.next

        return res
        
        
