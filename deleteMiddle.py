# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        curr=head
        while(curr):
            n+=1
            curr=curr.next
        
        if n<=1:
            return None
        mid=n//2
        # 0 1 / 2
        # 0 / 1
        # 0 1 2 / 3
        # 0 1 2 3 / 4
        curr=head
        index=0
        while(curr):
            if index+1==mid:
                temp=curr.next
                curr.next=curr.next.next
                temp.next=None
                break
            curr=curr.next
            index+=1
        return head


        

        

        
        
