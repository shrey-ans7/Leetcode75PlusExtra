class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        size=len(rooms)
        visited=set()
        def dfs(key):
            if key in visited:
                return
            visited.add(key)
            for next in rooms[key]:
                dfs(next)
            return
                           
        dfs(0)
        if len(visited)==size:
            return True
        return False
            

        
