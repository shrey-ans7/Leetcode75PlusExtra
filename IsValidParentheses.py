class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()
        tracker1={"(","{","["}
        for i in list(s):
           if i in tracker1:
               stack.append(i)
           else:
                if len(stack)==0:
                    return False
                tmp=stack.pop()
                if (i==")" and tmp=="(") or (i=="}" and tmp=="{") or (i=="]" and tmp=="["):
                    continue
                return False
        if(len(stack)==0):
            return True
        return False
                    
