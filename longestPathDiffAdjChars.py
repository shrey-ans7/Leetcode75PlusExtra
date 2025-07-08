import heapq
from typing import List

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        from collections import defaultdict
        
        
        tree = defaultdict(list)
        for child, par in enumerate(parent):
            tree[par].append(child)

        self.res = 1  
        def dfs(root):
            heap=[]
            for child in tree.get(root,[]):
                child_len=dfs(child)
                if s[root]!=s[child]:
                    heapq.heappush(heap,child_len)
                    if len(heap)>2:
                        heapq.heappop(heap)
            top2 = heap[0] if len(heap) > 0 else 0
            top1 = heap[1] if len(heap) > 1 else 0
            self.res=max(self.res,top1+top2+1)
            return max(top1,top2) + 1
        dfs(0)
        return self.res

                    
