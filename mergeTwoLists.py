# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iter1=list1
        iter2=list2
        iter3=ListNode()
        head=iter3
        while iter1!=None or iter2!=None:
            if iter1==None:
                while iter2!=None:
                    iter3.next=ListNode(iter2.val,None)
                    iter3=iter3.next
                    iter2=iter2.next
            elif iter2==None:
                while iter1!=None:
                    iter3.next=ListNode(iter1.val,None)
                    iter3=iter3.next
                    iter1=iter1.next
            elif iter1.val<iter2.val:
                iter3.next=ListNode(iter1.val,None)
                iter1=iter1.next
                iter3=iter3.next
            else:
                iter3.next=ListNode(iter2.val,None)
                iter2=iter2.next
                iter3=iter3.next
        head=head.next
        return head


                
            
        
