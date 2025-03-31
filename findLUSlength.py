class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        book={}
        for i in range(len(a)):
            book[a[:i+1]]=1
        for i in range(len(b)):
            if b[:i+1] not in book:
                book[b[:i+1]]=1
            else:
                book[b[:i+1]]+=1
        res=-1
        for subseq, occ in book.items():
            if occ==1:
                res=max(res,len(subseq))
        return res
                

        
