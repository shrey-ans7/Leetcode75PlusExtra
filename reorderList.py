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
