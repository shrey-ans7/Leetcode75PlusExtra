from collections import deque
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        queue1=deque(list("".join(s.split("-"))))
        queue2=deque()
        while queue1:
            i=0
            while queue1 and i<k:
                queue2.appendleft(queue1.pop().upper())
                i+=1
            queue2.appendleft("-")
        if queue2:
            queue2.popleft()
        return "".join(queue2)
        
