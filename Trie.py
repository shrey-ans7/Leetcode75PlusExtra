class Node:
    def __init__(self,flag):
        self.children = {}
        self.isWord=flag
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        currPrefix = self.root
        parent=None
        for char in word: 
            if char not in currPrefix:
                parent = Node(False)
                currPrefix[char] = parent
            parent = currPrefix[char]
            currPrefix = parent.children
        if parent:
            parent.isWord=True

    def search(self, word: str) -> bool:
        currPrefix = self.root
        for char in word: 
            if char not in currPrefix:
                return False
            parent = currPrefix[char]
            currPrefix = parent.children

        return parent.isWord

    def startsWith(self, prefix: str) -> bool:
        currPrefix = self.root
        for char in prefix:  
            if char not in currPrefix:
                return False
            currPrefix = currPrefix[char].children
        return True
