import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = {}
        for ch in s:
            freqs[ch] = freqs.get(ch, 0) + 1
        heap = [(-cnt, ch) for ch, cnt in freqs.items()]
        heapq.heapify(heap)
        res=[]
        prev=None
        while heap:
            curr=heapq.heappop(heap)
            char=curr[1]
            if prev and char==prev[1]:
                return ""
            res.append(char)
            freq=curr[0]
            if prev:
                heapq.heappush(heap,prev)
            if freq+1<0:
                prev=(freq+1,char)
            else:
                prev=None
        if prev:
            return ""
        return "".join(res)
            
            

        
