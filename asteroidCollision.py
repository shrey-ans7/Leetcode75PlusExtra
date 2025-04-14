class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for astr in asteroids:
            if stack:
                if stack[-1]>0 and astr<0:
                    mag=0
                    while stack and stack[-1]>0 and stack[-1]<abs(astr):
                        mag=stack.pop()

                    if stack and stack[-1]==abs(astr):
                        stack.pop()
                        continue
                    elif (not stack or stack[-1]<0):
                        stack.append(astr)
                    continue  
            stack.append(astr)
        return stack
                   
            
        
