# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        iter=head
        count=0
        while iter!=None:
            count+=1
            iter=iter.next
        iter=head
        if count==n==1:
            return None
        prev=iter
        iter=iter.next
        count-=1
        while(iter!=None):
            if count==n:
                prev.next=iter.next
                break
            elif count<n:
                head=iter
                break
            else:
                prev=prev.next
                iter=iter.next
                count-=1
        return head

                
                
