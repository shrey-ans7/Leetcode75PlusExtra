class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        size=len(digits)
        vocab={}
        alphas="abcdefghijklmnopqrstuvwxyz"
        count=0
        for i in range(2,10):
            if i!=7 and i!=9:
                vocab[str(i)]=alphas[count:count+3]
                count+=3
            else:
                vocab[str(i)]=alphas[count:count+4]
                count+=4
        visited=set()
        def dfs(i,combo):
            nonlocal digits
            if i==size:
                visited.add(combo)
                return
            for char in vocab[digits[i]]:
                dfs(i+1,combo+char)
            return
        dfs(0,"")
        if "" in visited:
            visited.remove("")
        return list(visited)

            
