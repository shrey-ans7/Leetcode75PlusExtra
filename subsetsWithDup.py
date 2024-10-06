class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        size=len(nums)
        res=set()
        stack=[]
        def dfs(i,stack):
            nonlocal res
            if i>=size:
                res.add(tuple(sorted(stack)))
                return
            #1. Skip
            res.add(tuple(sorted(stack)))
            dfs(i+1,stack)
            #2.Take
            stack.append(nums[i])
            res.add(tuple(sorted(stack)))
            dfs(i+1,stack)
            stack.pop()
            return
        dfs(0,stack)
        return list(res)

            
        
