# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        size1=0
        size2=0
        iterA=headA
        iterB=headB
        while(iterA):
            size1+=1
            iterA=iterA.next
        while(iterB):
            size2+=1
            iterB=iterB.next
        iterA=headA
        iterB=headB
        if size1>size2:
            while(size1!=size2):
                iterA=iterA.next
                size1-=1
        else:
            while(size1!=size2):
                iterB=iterB.next
                size2-=1
        while(iterA and iterB):
            if iterA==iterB:
                return iterA
            iterA=iterA.next
            iterB=iterB.next
        return None
        
