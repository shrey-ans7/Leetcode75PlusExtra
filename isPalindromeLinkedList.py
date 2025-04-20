# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow=head
        fast=head
        count=0
        while(slow):
            slow=slow.next
            count+=1
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(count)
        prev=None
        curr=head
        while(curr.next!=slow):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        curr.next=prev
        if count%2==1:
            slow=slow.next
        while(slow and curr):
            if slow.val!=curr.val:
                return False
            slow=slow.next
            curr=curr.next

        return True
        
        
        
