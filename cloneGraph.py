"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    nodes=None
    edges=None
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.nodes={}
        self.edges={}
        queue=deque()
        count=0
        start=node
        if not node:
            return node
        def createCopy(node):
            nghs=None
            if node.neighbors:
                nghs=[]
            if not node in self.edges.keys():
                self.nodes[node]=Node(node.val,nghs)
                self.edges[node]=self.nodes[node]
            else:
                self.nodes[node]=self.edges[node]
                self.nodes[node].neighbors=nghs
            if not node.neighbors:
                return
            for i in node.neighbors:
                queue.append(i)
                if not i in self.edges.keys():
                    ngh=Node(i.val)
                    self.edges[i]=Node(i.val)
                    #Shouldn't be ngh below
                    self.nodes[node].neighbors.append(self.edges[i]) 
                else:
                    self.nodes[node].neighbors.append(self.edges[i])
        queue.append(node)   
        while queue:
            node=queue.popleft()
            if node in self.nodes.keys():
                continue
            createCopy(node)


        return self.nodes[start]
