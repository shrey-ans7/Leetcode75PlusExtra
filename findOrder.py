class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={}
        skip=[0 for _ in range(numCourses)]
        for prereq in prerequisites:
            graph[prereq[1]]=graph.get(prereq[1],[])+[prereq[0]]
            skip[prereq[0]]=1
        visited=set()
        path=set()
        ans=[]
        count=0
        def dfs(node):
            nonlocal count
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            for ngh in graph.get(node,[]):
                if not dfs(ngh):
                    return False
            path.remove(node)
            visited.add(node)
            ans.append(node)
            count+=1
            return True
        for node in range(numCourses):
            if skip[node]==1:
                continue
            if not dfs(node):
                return []
        if numCourses==len(ans):
            ans.reverse()
            return ans
        return []


        
