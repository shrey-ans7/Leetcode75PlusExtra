class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(num,currSum,count,stack):
            if count==k:
                if currSum==n:
                    res.append(stack.copy())
                return
            if num>9 or currSum>n:#>2*n/k+1
                return
            dfs(num+1,currSum,count,stack)
            stack.append(num)
            dfs(num+1,currSum+num,count+1,stack)
            stack.pop()
            return
        dfs(1,0,0,[])
        return res

        
