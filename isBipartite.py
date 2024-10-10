from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        colors = [-1] * size

        for i in range(size):
            if colors[i] != -1:
                continue  # Node already colored, skip it.
            
            # Start BFS for this component.
            queue = deque([i])
            colors[i] = 0  # Start coloring with 0.

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        # Color with the opposite color of `node`.
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        # If the neighbor has the same color, graph isn't bipartite.
                        return False

        return True
