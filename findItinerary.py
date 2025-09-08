import heapq
from collections import defaultdict, deque
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build min-heaps of destinations for lexical order
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = deque()

        def dfs(airport: str) -> None:
            heap = graph[airport]
            # Consume all edges from this airport
            
            while heap:
                nxt = heapq.heappop(heap)
                dfs(nxt)
            route.appendleft(airport)
            

        dfs("JFK")
        return list(route)
