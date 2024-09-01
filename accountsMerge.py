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
            self.rank[root1] += self.rank[root2] #1
        
        return True

    def add(self, n):
        if n not in self.par:
            self.par[n] = n
            self.rank[n] = 1 #0

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        tracker={}
        unionFind = UnionFind()
        for i,acc in enumerate(accounts):
            unionFind.add(i)
            for email in acc[1:]:
                if email in tracker:
                    unionFind.union(tracker[email],i)
                else:
                    tracker[email]=i

        # Merge emails
        email_to_node = {}
        for email, index in tracker.items():
            root = unionFind.find(index)
            if root not in email_to_node:
                email_to_node[root] = set()
            email_to_node[root].add(email)
        
        # Build result
        res = []
        for index, emails in email_to_node.items():
            res.append([accounts[index][0]] + sorted(list(emails)))
        
        return res

            



        

        
