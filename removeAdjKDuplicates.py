class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[s[0]]
        count=k 
        counts=[1]
        for i in range(1,len(s)):
            if stack and stack[-1]==s[i]:
                count=counts[-1]+1
                stack.append(s[i])
                counts.append(count)
                if count==k:
                    while count>0:
                        stack.pop()
                        counts.pop()
                        count-=1
                i=i-k
            else:
                count=1
                counts.append(count)
                stack.append(s[i])
        return "".join(stack)
            
                
            
                
