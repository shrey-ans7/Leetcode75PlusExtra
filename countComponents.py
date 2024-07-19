class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        graph={}
        for edge in edges:
            if edge[0] in graph.keys():
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]]=[]
                graph[edge[0]].append(edge[1])
            if edge[1] in graph.keys():
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]]=[]
                graph[edge[1]].append(edge[0])
        visited=set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for ngh in graph[node]:
                dfs(ngh)
            return
        count=0
        if not graph.keys():
            return n
        for i in graph.keys():
            if i in visited:
                continue
            count+=1
            dfs(i)
        return count
        
