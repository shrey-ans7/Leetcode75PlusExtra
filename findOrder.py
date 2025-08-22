##Soln 1: DFS with Memo
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
        
#Soln 2: Topological Sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[bool]:
        graph={}
        in_degree=[0 for _ in range(numCourses)]
        for course in range(numCourses):
            graph[course]=[]
        for prereq in prerequisites:
            in_degree[prereq[0]]+=1
            graph[prereq[1]].append(prereq[0])
        queue=[]
        for crs in range(numCourses):
            if in_degree[crs]==0:
                queue.append(crs)
        index=0
        res=[]
        while index<len(queue):
            for crs in graph[queue[index]]:
                in_degree[crs]-=1
                if in_degree[crs]==0:
                    queue.append(crs)
            index+=1
        return queue if len(queue)==numCourses else []


        



        
