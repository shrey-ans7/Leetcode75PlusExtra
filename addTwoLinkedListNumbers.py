# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=[]
        iter1=l1
        while iter1!=None:
            num1.append(str(iter1.val))
            iter1=iter1.next
        num2=[]
        iter2=l2
        while iter2!=None:
            num2.append(str(iter2.val))
            iter2=iter2.next
        num1.reverse()
        num2.reverse()
        num1=int("".join(num1))
        num2=int("".join(num2))
        num3=list(str(num1+num2))
        head=ListNode()
        iter=head
        num3.reverse()
        for i in num3:
            iter.next=ListNode(int(i))
            iter=iter.next
        iter=head
        head=head.next
        iter.next=None
        return head

