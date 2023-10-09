class MyHashSet:

    def __init__(self):
        self.data=[None for _ in range(10**3)]

    def add(self, key: int) -> None:
        hash=key
        node=ListNode(key)
        if self.data[hash%len(self.data)]==None:
            self.data[hash%len(self.data)]=node
        else:
            iter=self.data[hash%len(self.data)]
            while iter!=None:
                if iter.val==key:
                    return
                elif iter.next==None:
                    iter.next=node
                iter=iter.next
    def remove(self, key: int) -> None:
        hash=key
        node=ListNode(key)
        if self.data[hash%len(self.data)]==None:
            return
        else:
            iter=self.data[hash%len(self.data)]
            prev=None
            if iter.val==key:
                self.data[hash%len(self.data)]=iter.next
                return
            elif iter.next==None:
                if iter.val==key:
                    self.data[hash%len(self.data)]=None
                return
            while iter!=None:
                if iter.val==key:
                    prev.next=iter.next
                    return
                prev=iter
                iter=iter.next
        

    def contains(self, key: int) -> bool:
        hash=key
        node=ListNode(key)
        if hash%len(self.data)==None:
            return False
        else:
            iter=self.data[hash%len(self.data)]
            while iter!=None:
                if iter.val==key:
                    return True
                iter=iter.next
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
