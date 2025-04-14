from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        chars="abcdefghijklmnopqrstuvwxyz"
        wordList=set(wordList)
        queue1=deque()
        queue2=deque()
        level=1
        size1=len(beginWord)
        size2=len(endWord)
        if size1!=size2:
            return 0
        queue1.append(beginWord)
        visited=set()
        while(queue1):
            curr=queue1.popleft()
            if curr==endWord:
                return level
            for idx in range(size1):
                for char in chars:
                    nextWord=curr[:idx]+char+curr[idx+1:]
                    if nextWord in wordList and nextWord not in visited:
                        queue2.append(nextWord)
                        visited.add(nextWord)
            if not queue1:
                while(queue2):
                    queue1.append(queue2.popleft())
                level+=1

        return 0


        
