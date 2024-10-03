#Not the most optimal, has a few experiments.
class Solution:
    def reverseWords(self, s: str) -> str:
        prev=" "
        stack=[]
        size=len(s)
        i=0
        count=0
        while(i<size):
            if s[i]==" ":
                if prev==" ":
                    i+=1
                    continue
                else:
                    stack.append(s[i])
                    prev=s[i]
                    count+=1
            else:
                stack.append(s[i])
                prev=s[i]
                count+=1
            i+=1
        
        while(stack[count-1]==" "):
            stack.pop()
            count-=1
        # j=0
        # while(j<count//2):
        #     placeholder=stack[j]
        #     stack[j]=stack[count-j-1]
        #     stack[count-j-1]=placeholder
        #     j+=1
        res="".join(stack)
        res=res.split(" ")
        res.reverse()
        prev=" "
        stack=[]
        for word in res:
                stack.append(word)
                stack.append(" ")
        stack.pop()

        return "".join(stack)
        
        
