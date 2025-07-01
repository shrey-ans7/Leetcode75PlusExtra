class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        alphas="abcdefghijklmnopqrstuvwxyz"
        book={alpha:index for index, alpha in enumerate(alphas)}
        size=len(word)
        tracker={}
        largest=-1
        index=-1
        for i in range(size-1,-1,-1):
            if largest<=book[word[i]]:
                index=i
                largest=book[word[i]]
                tracker[largest]=tracker.get(largest,[])+[index]
        return max(word[index:index+size-numFriends+1] for index in tracker.get(largest))




        
