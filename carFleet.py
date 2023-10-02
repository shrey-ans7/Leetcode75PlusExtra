class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        end=len(speed)
        tuples=[]
        for i in range(end):
            tuples.append([position[i],speed[i]])
        tuples.sort(key = lambda x:-x[0])
        i=0
        while i<end:
            time=(target-tuples[i][0])/tuples[i][1]
            if len(stack)==0:
                stack.append(time)
            elif stack[-1]<time:
                stack.append(time)
            i+=1
        return len(stack)
