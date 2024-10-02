import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.uniques=set()
        self.popped=[]
        heapq.heapify(self.popped)
        self.lower=1
        self.upper=1
        

    def popSmallest(self) -> int:
        ans=self.lower
        if self.lower==self.upper:
            self.lower+=1
            self.upper+=1
            return ans
        if self.popped:
            ans=heapq.heappop(self.popped)
            self.uniques.remove(ans)
            if self.popped:
                self.lower=self.popped[0]
            else:
                self.lower=self.upper
            return ans
        ans=self.lower
        self.lower=self.upper
        return ans
        

        

    def addBack(self, num: int) -> None:
        if num in self.uniques:
            return
        if num<self.upper:
            if num<self.lower:
                self.lower=num
            heapq.heappush(self.popped,num)
            self.uniques.add(num)
        return


        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
