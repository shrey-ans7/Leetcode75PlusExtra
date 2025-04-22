class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list: src → [dst1, dst2, …]
        graph = {i: [] for i in range(numCourses)}
        for dst, src in prerequisites:
            graph[src].append(dst)

        visited = set()  # courses we've fully checked (no cycles downstream)
        path    = set()  # recursion stack

        def dfs(crs: int) -> bool:
            if crs in path:
                # we’ve come back to something on our current stack → cycle
                return False
            if crs in visited:
                # already checked this node, and it was safe
                return True

            path.add(crs)
            for nxt in graph[crs]:
                if not dfs(nxt):
                    return False
            path.remove(crs)

            # mark as safe
            visited.add(crs)
            return True

        # try to DFS from every course
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
