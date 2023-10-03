"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        count=0
        iter=head
        tracker={}
        container=[]
        while iter!=None:
            tracker[iter]=count
            container.append(Node(iter.val))
            count+=1
            iter=iter.next
        iter=head
        for i in range(count):
            if i==count-1:
                container[i].next=None
            else:
                container[i].next=container[i+1]
            if iter.random in tracker.keys():
                container[i].random=container[tracker[iter.random]]
            else:
                container[i].random=None
            iter=iter.next
        if count==0:
            return None
        head=container[0]
        return head
