class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited=set()
        graph={}
        edges=set()
        for edge in connections:
            graph[edge[0]]=graph.get(edge[0],[])+[edge[1]]
            edges.add((edge[0],edge[1]))
            graph[edge[1]]=graph.get(edge[1],[])+[edge[0]]
        count=0
        def dfs(node):
            if node in visited:
                return
            nonlocal count
            visited.add(node)
            for ngh in graph.get(node,[]):
                if ngh in visited:
                    continue
                if (node,ngh) in edges:
                    count+=1
                dfs(ngh)
            return
        
        dfs(0)
        return count
        
