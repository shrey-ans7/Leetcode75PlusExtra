class Node:
    def __init__(self, val, prev=None, next= None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = Node(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        if steps==0:
            return self.curr.val
        elif self.curr.prev==None:
            return self.curr.val
        else:
            self.curr=self.curr.prev
            return self.back(steps-1)
        

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
