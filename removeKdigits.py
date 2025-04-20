class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for digit in num:
            while k and stack and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        start=0
        while start<len(stack) and stack[start]=="0":
            start+=1
        stack=stack[start:len(stack)-k]
        if not stack:
            stack=["0"]
        return "".join(stack)

        
