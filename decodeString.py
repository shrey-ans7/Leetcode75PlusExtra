class Solution:
    def decodeString(self, s: str) -> str:
        end=len(s)
        stack=[]
        balance=0
        buffer=""
        for char in s:
            if char=="]":
                while(stack[-1]!="["):
                    buffer+=stack.pop()
                stack.pop()
                length=""
                while(stack and stack[-1].isdigit()):
                    length+=stack.pop()
                length=int(length[::-1])
                stack.append(buffer*length)
                buffer=""
            else:
                stack.append(char)
        res=""
        for word in stack:
            res+=word[::-1]
        return res
            
            

        
