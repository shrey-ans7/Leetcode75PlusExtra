# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i,aList in enumerate(lists):
            if aList:
                heapq.heappush(heap,(aList.val,i,aList))  
            
        if not heap:
            return None
        dummy=ListNode()
        curr=dummy
        while heap:
            val,i,nextNode=heapq.heappop(heap)
            curr.next=nextNode
            curr=curr.next
            if nextNode.next:
                heapq.heappush(heap,(nextNode.next.val,i,nextNode.next))  
        
        return dummy.next
