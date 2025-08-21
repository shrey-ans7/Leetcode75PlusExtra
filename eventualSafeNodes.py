from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # Build reverse graph and out-degree (in original)
        rev = [[] for _ in range(n)]
        out = [0] * n
        for u, nbrs in enumerate(graph):
            out[u] = len(nbrs)          # out-degree in original
            for v in nbrs:
                rev[v].append(u)        # reverse edge: v -> u

        # Start from terminal nodes (out-degree == 0)
        queue = [i for i in range(n) if out[i] == 0]

        # Kahn's algorithm on reverse graph
        index = 0
        while index < len(queue):
            u = queue[index]
            for p in rev[u]:            # predecessors in original graph
                out[p] -= 1
                if out[p] == 0:
                    queue.append(p)
            index += 1

        # All processed nodes are safe
        return sorted(queue)
