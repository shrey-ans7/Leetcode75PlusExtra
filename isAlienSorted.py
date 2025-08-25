#Soln 1:
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order={char:i for i,char in enumerate(order)}
        def in_order(word1, word2):
            for c1, c2 in zip(word1,word2):
                if c1!=c2:
                    return order[c1]<order[c2]
            return len(word1)<=len(word2)
        for i in range(len(words)-1):
            if not in_order(words[i],words[i+1]):
                return False
        return True
        
#Soln 2:
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        import heapq
        heap=[]
        order={char:i for i,char in enumerate(order)}
        tracker={}
        for word in words:
            word_tup=tuple([order[char] for char in word])
            tracker[word_tup]=word
            heapq.heappush(heap,word_tup)
        index=0
        while heap:
            word_tup=heapq.heappop(heap)
            if words[index]!=tracker[word_tup]:
                return False
            index+=1
        return True
        
        
