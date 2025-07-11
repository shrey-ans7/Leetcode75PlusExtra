class Node:
    def __init__(self):
        self.children={}
        self.isWord=False

class WordDictionary:

    def __init__(self):
        self.root=Node()


    def addWord(self, word: str) -> None:
        children=self.root.children
        for char in word:
            if char not in children:
                child=Node()
                children[char]=child
            else:
                child=children[char]
            children=child.children
        child.isWord=True
        return
        

    def search(self, word: str) -> bool:
        def dfs(i,curr):
            nonlocal word
            if i==len(word):
                return curr.isWord
            if word[i]==".":
                for child in curr.children.values():
                    if dfs(i+1,child):
                        return True
                return False
            else:
                child=curr.children.get(word[i],None)
                if not child:
                    return False
                else:
                    return dfs(i+1,child)
        return dfs(0,self.root)


        
