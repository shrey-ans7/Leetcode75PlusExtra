class MinStack:

    def __init__(self):
        self.data=[]
        self.mins=[]

    def push(self, val: int) -> None:
        if len(self.data)!=0:
            if self.mins[-1]>val:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)
        self.data.append(val)

    def pop(self) -> None:
        self.mins.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
