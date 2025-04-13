class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eqs={}
        graph={}
        for i,vars in enumerate(equations):
            eqs[(vars[0],vars[1])]=values[i]
            eqs[(vars[1],vars[0])]=1/values[i]
            graph[vars[0]]=graph.get(vars[0],[])+[vars[1]]
            graph[vars[1]]=graph.get(vars[1],[])+[vars[0]]
        from collections import deque
        res=[]
        for query in queries:
            if query[0] not in graph or query[1] not in graph:
                res.append(-1.0)
            else:
                visited=set()
                queue1=deque()
                queue1.append((query[0],1))
                goal=query[1]
                visited.add(query[0])
                found=False
                while(queue1):
                    par=queue1.popleft()
                    if par[0]==goal:
                        res.append(par[1])
                        found=True
                        break
                    for ngh in graph.get(par[0],[]):
                        if ngh in visited:
                            continue
                        queue1.append((ngh,eqs[(par[0],ngh)]*par[1]))
                        visited.add(ngh)
                if not found:
                    res.append(-1.0)

        return res
