class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = {}
        for edge in edges:
            if edge[0]==edge[1]:
                return False
            if edge[0] in graph.keys():
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]]=[edge[1]]
            if edge[1] in graph.keys():
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]]=[edge[0]]
        if n<=1:
            return True
        def dfs(node,prev):
            nonlocal visited
            visited.add(node)
            flag=True
            for i in graph[node]:
                if i==prev:
                    continue
                elif i in visited:
                    flag = False
                    return flag
                flag = flag and dfs(i,node)
                if not flag:
                    return flag
            return flag
        flag=dfs(0,n)
        print(visited)
        if len(visited)==n:
            return flag
        else:
            return False

            
        
        
