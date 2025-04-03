from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        visited=[-1 for _ in range(n)]
        queue1=deque()
        queue2=deque()
        for index in range(n):
            if visited[index]!=-1:
                continue
            queue1.append(index)
            visited[index]=0
            while(queue1):
                node=queue1.pop()
                color=visited[node]
                for ngh in graph[node]:
                    nghColor=visited[ngh]
                    if nghColor==-1:
                        visited[ngh]=1-color
                    elif nghColor!=1-color:
                        return False
                    else:
                        continue
                    queue2.append(ngh)
                if not queue1:
                    while(queue2):
                        queue1.append(queue2.pop())
        return True





        
