class Solution:
    def helper(self, n:int, oc: int, cc: int, stack: List[str], strings: List[str]):
        
        if oc==cc==n:
            string="".join(stack)
            strings.append(string)
            return 
        if oc<n:
            stack.append("(")
            self.helper(n, oc+1, cc, stack, strings)
            stack.pop()
        if cc<oc:
            stack.append(")")
            self.helper(n, oc, cc+1, stack, strings)
            stack.pop()
        return 


            

    def generateParenthesis(self, n: int) -> List[str]:
        open_count=0
        closed_count=0
        strings=[]
        stack = []
        self.helper(n, 0, 0, stack, strings)
        return strings
        
