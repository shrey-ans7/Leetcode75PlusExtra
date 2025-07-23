#Soln 1 (New)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast.next:
            slow=slow.next
            fast=fast.next.next if fast.next.next else fast.next
        prev=None
        itr=slow.next
        slow.next=None
        while itr:
            nxt=itr.next
            itr.next=prev
            prev=itr
            itr=nxt
        itr1=head
        itr2=prev
        while itr2:
            nxt1=itr1.next
            nxt2=itr2.next
            itr1.next=itr2
            itr2.next=nxt1
            itr1.next=itr2
            itr1=nxt1
            itr2=nxt2
        return 

#Soln 2 (Old)        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack=[]
        iter=head
        count=0
        while iter!=None:
            stack.append(iter)
            iter=iter.next
            count+=1
        
        iter=stack.pop(0)
        head=iter
        for i in range(1,count):
            if i%2==0:
                iter.next=stack.pop(0)
            else:
                iter.next=stack.pop()
            iter=iter.next
        iter.next=None
        return head
