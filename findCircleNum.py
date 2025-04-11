class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size=len(isConnected)
        if size==1:
            return 1
        if size==2:
            if isConnected[0][1]==1:
                return 1
            else:
                return 2
        visited=set()
        province=set()
        def dfs(node):
            if node in province:
                return
            province.add(node)
            count=0
            for ngh in isConnected[node]:
                if ngh==1:
                    dfs(count)
                count+=1
            return
        count=0
        for i in range(size):
            if i in visited:
                continue
            dfs(i)
            visited.update(province)
            count+=1
            if len(visited)==size:
                return count
            province=set()
        return count


        
