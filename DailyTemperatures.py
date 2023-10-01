class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        end=len(temperatures)
        time_stack=[None for i in range(end)]
        stack = []
        stack.append([0,temperatures[0]])
        i=1
        while i<end:
            if len(stack)==0:
                stack.append([i,temperatures[i]])
                i+=1
            elif stack[-1][1]>=temperatures[i]:
                stack.append([i,temperatures[i]])
                i+=1   
            else:
                data=stack.pop()
                time_stack[data[0]]=i-data[0]
        for i in range(end):
            if time_stack[i]==None:
                time_stack[i]=0
        return time_stack     
