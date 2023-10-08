class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]#set()
        stack=[]
        total=0
        def dfs(i):
            nonlocal total
            nonlocal res
            nonlocal stack
            if i>=len(candidates):
                return 
            total+=candidates[i]
            stack.append(candidates[i])
            if total>=target:
                if total==target:
                    res.append(stack.copy())
                total-=candidates[i]
                stack.pop()
                dfs(i+1)
                return

            
            # dfs(i+1)
            dfs(i)
            
            stack.pop()
            total-=candidates[i]
        
            dfs(i+1)
            return
        dfs(0)
        return res
