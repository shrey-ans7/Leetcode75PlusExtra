import heapq
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mins=[]
        k=0
        heapq.heapify(mins)
        for price in prices:
            if k==2:
                heapq.heappush(mins,max(heapq.heappop(mins),-price))
            else:
                heapq.heappush(mins,-price)
                k+=1
        total=0
        for price in mins:
            total+=abs(price)
        if total>money:
            return money
        return money-total
        
