class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = {}

    def find(self, n):
        if self.par[n] != n:
            self.par[n] = self.find(self.par[n])  # Path compression
        return self.par[n]

    def union(self, fir, sec):
        root1 = self.find(fir)
        root2 = self.find(sec)
        
        if root1 == root2:
            return False
        
        # Union by rank
        if self.rank[root1] > self.rank[root2]:
            self.par[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.par[root1] = root2
        else:
            self.par[root2] = root1
            self.rank[root1] += 1
        
        return True

    def add(self, n):
        if n not in self.par:
            self.par[n] = n
            self.rank[n] = 0


class Node:
    def __init__(self,details):
        self.name=details[0]
        self.emails=set(details)
        self.emails.remove(self.name)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        tracker={}
        unionFind = UnionFind()
        for acc in accounts:
            node=Node(acc)
            unionFind.add(node)
            for email in node.emails:
                if email in tracker:
                    unionFind.union(tracker[email],node)
                else:
                    tracker[email]=node

        # Merge emails
        email_to_node = {}
        for email, node in tracker.items():
            root = unionFind.find(node)
            if root not in email_to_node:
                email_to_node[root] = set()
            email_to_node[root].add(email)
        
        # Build result
        res = []
        for node, emails in email_to_node.items():
            res.append([node.name] + sorted(list(emails)))
        
        return res

            



        

        
