import heapq
from typing import List

class Node:
    def __init__(self, curr, cost, steps):
        self.curr = curr
        self.cost = cost
        self.steps = steps
    
    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        if self.cost == other.cost:
            return self.steps < other.steps
        return False
    def __str__(self):
        return str((self.curr,self.cost,self.steps))

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for flight in flights:
            if flight[0] in graph:
                graph[flight[0]].append((flight[1], flight[2]))
            else:
                graph[flight[0]] = [(flight[1], flight[2])]
        
        # Min-heap priority queue
        queue = [Node(src, 0, 0)]
        visited=set()
        k+=1
        while queue:
            node = heapq.heappop(queue)
            if node.curr == dst:
                return node.cost
            if (node.curr,node.steps) in visited:
                continue
            # Skip if steps exceed the limit
            if node.steps+1 > k:
                continue
            # Need to add tuple instead of just the index,
            # as we could choose more expensive node with fewer steps,
            # so net distance within k steps is cheaper overall.
            visited.add((node.curr,node.steps)) 
            for ngh, price in graph.get(node.curr, []):
                new_cost = node.cost + price
                if (ngh,node.steps+1) not in visited: 
                    # Don't add to visited here as we edge lists of a node
                    # as in its nghs' may not be in sorted order (by wts/steps)
                    next=Node(ngh, new_cost, node.steps + 1)
                    heapq.heappush(queue, next)
        return -1
