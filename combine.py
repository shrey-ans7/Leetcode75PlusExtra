class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(i,stack):
            nonlocal res,k,n
            if i>n:
                if len(stack)==k:
                    res.append(stack.copy())
                return
            
            stack.append(i)
            dfs(i+1,stack)
            stack.pop()
            dfs(i+1,stack)
            return
        dfs(1,[])
        return res

        
