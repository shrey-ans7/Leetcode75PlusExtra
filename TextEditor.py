class Node:
    def __init__(self,char,next=None,prev=None):
        self.char=char
        self.next=None
        self.prev=None
from collections import deque
class TextEditor:

    def __init__(self):
        self.head=None
        self.tail=None
        self.curr=None
    

    def addText(self, text: str) -> None:
        for char in text:
            node=Node(char)
            if not self.head:
                self.head=self.tail=self.curr=node
                continue
            if not self.curr:
                node.next=self.head
                self.curr=node
                self.head.prev=node
                self.head=node
                continue
            if self.curr.next:
                self.curr.next.prev=node
            node.next=self.curr.next
            node.prev=self.curr
            self.curr.next=node
            self.curr=node
        if not self.curr.next:
            self.tail=self.curr
        return 
            
    def deleteText(self, k: int) -> int:
        count=0
        if not self.curr:
            return count
        next_node=self.curr.next
        while count<k and self.curr:
            self.curr=self.curr.prev
            count+=1
        if not self.curr:
            if not next_node:
                self.head=self.tail=self.curr=None
            else:
                self.head=next_node
                self.head.prev=None
        else:
            if not next_node:
                self.tail=self.curr
                if not self.curr.prev:
                    self.head=self.curr
                self.curr.next=None
            else:
                self.curr.next=next_node
                next_node.prev=self.curr
                if not self.curr.prev:
                    self.head=self.curr
        return count

    def cursorLeft(self, k: int) -> str:
        while self.curr and k:
            self.curr=self.curr.prev
            k-=1
        if not self.curr:
            return ""
        queue=deque()
        itr=self.curr
        count=0
        while itr and count<10:
            queue.appendleft(itr.char)
            itr=itr.prev
            count+=1
        return "".join(queue)
        

    def cursorRight(self, k: int) -> str:
        if not self.head:
            return ""
        if not self.curr:
            self.curr=self.head
            k-=1
        while self.curr.next and k:
            self.curr=self.curr.next
            k-=1

        queue=deque()
        itr=self.curr
        count=0
        while itr and count<10:
            queue.appendleft(itr.char)
            itr=itr.prev
            count+=1
        return "".join(queue)
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
