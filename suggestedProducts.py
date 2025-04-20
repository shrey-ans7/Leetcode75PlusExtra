class Prefix:
    def __init__(self,name,is_product):
        self.prefixes={}
        self.isProduct=is_product
        self.products=[name]
    def __repr__(self):
        return str(self.prefixes)+str(self.products)+str(self.isProduct)
class Trie:
    def __init__(self):
        self.prefixes={}
    

    def addProduct(self,product):
        prefix=self.prefixes
        for char in product:
            if char in prefix:
                next_prefix=prefix[char]
                next_prefix.products.append(product)
            else:
                next_prefix=Prefix(product,False)
                prefix[char]=next_prefix
            prefix=next_prefix.prefixes
        next_prefix.isProduct=True

    def searchPrefix(self,product,response):
        prefix=self.prefixes
        index=0
        for char in product:
            if char in prefix:
                next_prefix=prefix[char]
                response[index]=sorted(next_prefix.products)[:3]
                prefix=next_prefix.prefixes
                index+=1
            else:
                break


        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie:Trie=Trie()
        for product in products:
            trie.addProduct(product)
        response=[[] for _ in range(len(searchWord))]
        trie.searchPrefix(searchWord,response)
        return response

        
        
