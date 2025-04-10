#Soln 1
from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()
        

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

#Soln 2
from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue=deque()
        

    def ping(self, t: int) -> int:
        count=1
        for req in reversed(self.queue):
            if req>=t-3000:
                count+=1
            else:
                break
        self.queue.append(t)
        return count


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
