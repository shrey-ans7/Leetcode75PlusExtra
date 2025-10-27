from typing import List
from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}
        
        # Build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Invalid case: prefix problem
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        print(graph)
        # DFS-based topological sort
        visited = {}
        res = []
        
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = False  # mark as visiting
            for nei in graph[char]:
                if not dfs(nei):
                    return False
            visited[char] = True   # mark as done
            res.append(char)
            return True
        
        for c in in_degree:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
