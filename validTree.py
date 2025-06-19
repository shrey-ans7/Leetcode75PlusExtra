class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph={}
        for edge in edges:
            graph[edge[0]]=graph.get(edge[0],[])+[edge[1]]
            graph[edge[1]]=graph.get(edge[1],[])+[edge[0]]
        path=set()
        count=0
        def dfs(node, prev):
            if node in path:
                return False
            nonlocal count
            count+=1
            path.add(node)
            for ngh in graph.get(node,[]):
                if ngh==prev:
                    continue
                if not dfs(ngh,node):
                    return False
            path.remove(node)
            return True
        return dfs(0,n) and count==n



       
