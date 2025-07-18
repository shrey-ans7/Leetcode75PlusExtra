class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res=-1
        path=set()
        tracker={}
        visited=set()
        def dfs(curr, count):
            nonlocal res
            if curr in path:
                res=max(res,len(path)-max(0,tracker[curr]))
                return
            if curr in visited:
                return
            visited.add(curr)
            path.add(curr)
            tracker[curr]=count+1
            ngh=edges[curr]
            if ngh!=-1:
                dfs(ngh,count+1)
            del tracker[curr]
            path.remove(curr)
            return
        for node in range(len(edges)):
            if node in visited:
                continue
            dfs(node,-1)
        return res

        
        

        
