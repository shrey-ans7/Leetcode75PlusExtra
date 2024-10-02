from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=deque(word1)
        word2=deque(word2)
        res=[]
        i=0
        while (word1 or word2):
            if word1 and i%2==0:
                res.append(word1.popleft())
            elif word2:
                res.append(word2.popleft())
            i+=1
        return "".join(res)
